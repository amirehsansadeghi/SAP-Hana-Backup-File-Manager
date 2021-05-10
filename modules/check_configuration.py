import configparser
import os 

def configuration_check():
    snd_dict = dict ()
    dev_dict = dict ()
    qua_dict = dict ()
    prd_dict = dict ()
    sdb_dict = dict ()
    email_dict = dict()
    email_send_list = dict()
    
    if os.path.isfile('/etc/hanabkmgmt.conf'):
        config = configparser.RawConfigParser()
        config.read('/etc/hanabkmgmt.conf')
        general_dict = dict(config.items('GENERAL'))
        snd_config_data = dict(config.items('HANA SND'))
        dev_config_data = dict(config.items('HANA DEV'))
        qua_config_data = dict(config.items('HANA QUA'))
        prd_config_data = dict(config.items('HANA PRD'))
        sdb_config_data = dict (config.items('HANA SYSTEMDB'))
        email_config_data = dict(config.items('EMAIL SETTINGS'))
        email_send_list = dict(config.items('EMAIL LIST'))
        
    if snd_config_data['enabled'].lower() == 'true':
        snd_dict['enabled'] = snd_config_data['enabled'].lower()
        snd_dict['name']=snd_config_data['sid_name']
        snd_dict['action'] = snd_config_data['action'].lower()
        snd_dict['log_file'] = snd_config_data['log_file']
        if snd_dict['log_file'][-1] != '/':
            snd_dict['log_file']=snd_dict['log_file']+'/'
        snd_dict['data_file'] = snd_config_data['data_file']
        if snd_dict['data_file'][-1] != '/':
            snd_dict['data_file']=snd_dict['data_file']+'/'
    else : 
        snd_dict['enabled'] = snd_config_data['enabled'].lower()

    if dev_config_data['enabled'].lower() == "true" :
        dev_dict['enabled'] = dev_config_data['enabled'].lower()
        dev_dict['name'] = dev_config_data['sid_name']
        dev_dict['action'] = dev_config_data['action'].lower()
        dev_dict['log_file'] = dev_config_data['log_file']
        if dev_dict['log_file'][-1] != '/':
            dev_dict['log_file']=dev_dict['log_file']+'/'
        dev_dict['data_file'] = dev_config_data['data_file']
        if dev_dict['data_file'][-1] != '/':
            dev_dict['data_file']=dev_dict['data_file']+'/'
    else :
        dev_dict['enabled'] = dev_config_data['enabled'].lower()

    if qua_config_data['enabled'].lower() == "true":
        qua_dict['enabled'] = qua_config_data['enabled'].lower()
        qua_dict['name'] = qua_config_data['sid_name']
        qua_dict['action'] = qua_config_data['action'].lower()
        qua_dict['log_file'] = qua_config_data['log_file']
        if qua_dict['log_file'][-1] != '/':
            qua_dict['log_file']=qua_dict['log_file']+'/'
        qua_dict['data_file'] = qua_config_data['data_file']
        if qua_dict['data_file'][-1] != '/':
            qua_dict['data_file']=qua_dict['data_file']+'/'
    else:
        qua_dict['enabled'] = qua_config_data['enabled'].lower()
    
    if prd_config_data['enabled'].lower() == 'true':
        prd_dict['enabled'] = prd_config_data['enabled'].lower()
        prd_dict['name'] = prd_config_data['sid_name']
        prd_dict['action'] = prd_config_data['action'].lower()
        prd_dict['log_file'] = prd_config_data['log_file']
        if prd_dict['log_file'][-1] != '/':
            prd_dict['log_file']=prd_dict['log_file']+'/'
        prd_dict['data_file'] = prd_config_data['data_file']
        if prd_dict['data_file'][-1] != '/':
            prd_dict['data_file']=prd_dict['data_file']+'/'
    else:
        prd_dict['enabled'] = prd_config_data['enabled'].lower()
    
    if sdb_config_data['enabled'].lower() == 'true':
        sdb_dict['enabled'] = sdb_config_data['enabled'].lower()
        sdb_dict['name'] = sdb_config_data['sid_name']
        sdb_dict['action'] = sdb_config_data['action'].lower()
        sdb_dict['log_file'] = sdb_config_data['log_file']
        if sdb_dict['log_file'][-1] != '/':
            sdb_dict['log_file']=sdb_dict['log_file']+'/'
        sdb_dict['data_file'] = sdb_config_data['data_file']
        if sdb_dict['data_file'][-1] != '/':
            snd_dict['data_file']=snd_dict['data_file']+'/'
    else:
        sdb_dict['enabled'] = sdb_config_data['enabled'].lower()
   
    if email_config_data['enabled'].lower() == 'true':
        email_dict['enabled']=email_config_data['enabled'].lower()
        email_dict['smtp_server']=email_config_data['smtp_server']
        email_dict['smtp_port'] = email_config_data['smtp_port']
        email_dict['tls']=email_config_data['smtp_tls']
        email_dict['sender_username']=email_config_data['sender_username']
        email_dict['sender_password']=email_config_data['sender_password']
    else:
        email_dict['enabled'] = email_config_data['enabled'].lower()
 
    if general_dict['target_path'] != '' : 
        return general_dict , snd_dict , dev_dict , qua_dict , prd_dict , sdb_dict,email_dict,email_send_list
    else:
        print('config file does not exists in /etc/hanabkmgmt.conf')