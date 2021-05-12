import smtplib,socket
from email.mime.text import MIMEText
from sys import exit

def test_email(smtp_server,smtp_port,smtp_username,smtp_password,tls,mail_address):
    message = """
    Hi there

    This is a email for test SAP HANA Backup Manager agent connected to mail server.
    
    email server and connections is worked corectly

    Thankyou
    
    """
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        msg = MIMEText(message)
        msg['Subject'] = "HANA Backup File Manager Agent"
        msg['From'] = smtp_username
        msg['To'] = mail_address
        debuglevel = True
        mail = smtplib.SMTP(smtp_server, smtp_port)
        mail.set_debuglevel(debuglevel)
        if tls =='yes' : mail.starttls()
        mail.login(smtp_username, smtp_password)
        mail.sendmail(smtp_username, mail_address, msg.as_string())
        mail.quit()
        exit()

def sendemail(smtp_server,smtp_port,smtp_username,smtp_password,tls,mail_address,function_message):
    
    message = '''
Dear SAP Basis Administrator
Hello 
this is agent runned on %s server hostname 
the actions mentioned below are according to your configuration file, please check: 

 %s

Best Regards
SAP HANA Backup File Manager Agent
    ''' %(socket.gethostname(),function_message)
    
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        msg =MIMEText(message)
        msg['Subject'] = "SAP HANA Backup File Manager Agent"
        msg['From'] = smtp_username
        #debuglevel = True
        mail = smtplib.SMTP(smtp_server, smtp_port)
        #mail.set_debuglevel(debuglevel)
        if tls =='yes' : mail.starttls()
        mail.login(smtp_username, smtp_password)
        for item,email_address in mail_address.items():
            msg['To'] = email_address
            mail.sendmail(smtp_username, email_address, msg.as_string())
        mail.quit()