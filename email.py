import smtplib
import os
import base64

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# smtp connection variables
smtp_ssl_host = os.environ['HOST']
smtp_ssl_port = os.environ['PORT_SMTP']

# credentials
email_user = os.environ['EMAIL_USER']
email_pw = os.environ['EMAIL_PW']

def send_email(event, context):
    # getting the attributes from the event
    email_type = event.get('attributes').get('type')
    text = event.get('attributes').get('text')
    subject = event.get('attributes').get('subject')
    from_addr = event.get('attributes').get('from_addrs')
    to_addrs = event.get('attributes').get('to')

    # email_type can be one of the following values:
    # 1 - text with html report
    # 2 - text only
    if email_type == '1':
        # if its an html report we will get it from event.data
        attachment_data = base64.b64decode(event.get('data'))
        attachment_name = event.get('attributes').get('attachment_name')

        # creating a multipart email
        email = MIMEMultipart('alternative')
        # creating a attachment object with the report
        attachment = MIMEBase('application', 'octet-stream')
        attachment.set_payload(attachment_data)
        encoders.encode_base64(attachment)
        attachment.add_header('content-disposition', f'attachment; filename={attachment_name}')
        # attaching the parts to the email
        email.attach(MIMEText(text))
        email.attach(attachment)
    elif email_type == '2':
        # creating a text email
        email = MIMEText(text)
    
    # adding the standard variables
    email['subject'] = subject
    email['from'] = from_addr
    email['to'] = to_addrs

    # connecting to smtp server with SSL
    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    # logging in
    server.login(email_user, email_pw)
    # sending the email
    server.sendmail(from_addr, to_addrs, email.as_string())
    # exiting
    server.quit()
