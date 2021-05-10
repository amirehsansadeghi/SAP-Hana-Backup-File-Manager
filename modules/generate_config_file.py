def generate():
    with open('/etc/hanabkmgmt.conf','w') as config_file : 
        config_file.write("""
##### Please fill in the fields in each section if needed #####
##### NOTE : DONT CHANGE HEADER FILEDS BETWEEN [...]
[GENERAL]
target_path = /tmp/
#### Please fill delete time per week
#### for example in the below config means delete older backup file after 4 week 
delete_archive = false
delete_time = 4

[EMAIL SETTINGS]
enabled = false
smtp_server = smtp.mydomain.com
smtp_port = 587
smtp_tls = yes
sender_username = username
sender_password = password

#### for the email list please add the recivers email address 
#### ext. EMAIL1 = info@mydomain.com or email1 = info@mydomain.com 
#### ext. EMAIL2 = admin@mydomain.com or email2 = admin@mydomain.com
#### NOTICE : you can add unlimited recivers email address like the above template
[EMAIL LIST]
email1 = info@mydomain.com
email2 = admin@mydomain.com

[HANA SND]
enabled = false
sid_name = SND
# action just you will be set mv for move files 
# or set cp for copy files 
# default value is cp
action = cp
log_file = /tmp/log/
data_file = /tmp/data

[HANA DEV]
enabled = false
sid_name = DEV
# action just you will be set mv for move files 
# or set cp for copy files 
# default value is cp
action = cp
log_file = /tmp/log/
data_file = /tmp/data

[HANA QUA]
enabled = false
sid_name = QUA
# action just you will be set mv for move files 
# or set cp for copy files 
# default value is cp
action = cp
log_file = /tmp/log/
data_file = /tmp/data

[HANA PRD]
enabled = false
sid_name = PRD
# action just you will be set mv for move files 
# or set cp for copy files 
# default value is cp
action = cp
log_file = /tmp/log/
data_file = /tmp/data

[HANA SYSTEMDB]
enabled = false
sid_name = SYSTEMDB
# action just you will be set mv for move files 
# or set cp for copy files 
# default value is cp
action = cp
log_file = /tmp/log/
data_file = /tmp/data

""")