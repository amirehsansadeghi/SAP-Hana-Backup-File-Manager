import smtplib
from email.mime.text import MIMEText

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

def sendemail(smtp_server,smtp_port,smtp_username,smtp_password,tls,mail_address,function_message):
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        msg = MIMEText(message)
        msg['Subject'] = "HANA Backup File Manager Agent"
        msg['From'] = smtp_username
        msg['To'] = mail_address
        #ebuglevel = True
        mail = smtplib.SMTP(smtp_server, smtp_port)
        #mail.set_debuglevel(debuglevel)
        if tls =='yes' : mail.starttls()
        mail.login(smtp_username, smtp_password)
        mail.sendmail(smtp_username, mail_address, function_message.as_string())
        mail.quit()