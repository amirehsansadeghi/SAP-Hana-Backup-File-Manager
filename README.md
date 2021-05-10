Hana Backup Management Agent

if you want show the operations on the console please use -v switch like 
blow command : 

#hanabkmgmt -v 

if you want recieve email after operation is complete operations, first you 
set email server connection string in the config file and then use test email switch for 
make sure it worked as fine , for do that you can use command with --test-email
for example :

#hanabkmgmt.py --test-email test@mydomain.com
