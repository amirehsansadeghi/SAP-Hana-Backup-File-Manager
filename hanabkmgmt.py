from modules import get_time_date 
from modules import check_configuration  as configuration
from modules import archive_bk_files as archive
from modules import folder_check_create as fcc
from modules import generate_config_file
from modules import manage_archives
from modules import email_gateway
from operation_files import sandbox,development,quality,production,systemdb
from os import path
import sys

verbos='false'
if (sys.version_info.major == 3 )  and (sys.version_info.minor >= 2 ) : 
    if path.exists('/etc/hanabkmgmt.conf'):
        general_dict ,snd_dict,dev_dict , qua_dict , prd_dict ,sdb_dict,email_dict,email_send_list = configuration.configuration_check()
        if len(sys.argv) >= 2 :
            if sys.argv[1] == '--test-email' :
                if email_dict['enabled'] == 'true':
                    email_gateway.test_email(email_dict['smtp_server'],
                    email_dict['smtp_port'],email_dict['sender_username'],
                    email_dict['sender_password'],email_dict['tls'],sys.argv[2])
            if sys.argv[1] == '-v' :
                verbos='true'           
     
        snd=sandbox.manage_file(general_dict,snd_dict)
        dev=development.manage_file(general_dict,dev_dict)
        qua=quality.manage_file(general_dict,qua_dict)
        prd=production.manage_file(general_dict,prd_dict)
        sdb=systemdb.manage_file(general_dict,prd_dict)
        
        if verbos=='true':
            if snd!='' : print(snd)
            if dev!='' : print(dev)
            if qua!='' : print(qua)
            if prd!='' : print(prd)
            if sdb!='' : print(sdb)
    
    else : 
        generate_config_file.generate()
        print(''' NOTE : the hanabkmgmt agent config file is not fount in the /etc/hanabkmgmt.conf path.
        we are generate it the same path please edit this file.
        if you want send email after every complete actions, we advise to you test your connection between
        this agent and mail server from the below command :

        hanabkmgmt --test-email [your mail address]
        
         ''')
else : 
    print ('DEPRECATION: Python 2.7 reached the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 is no longer maintained.')
     