import mimetypes
import smtplib
from datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate

today = datetime.today().strftime('%d-%m-%Y')


class EmailClient:
    def __init__(self, username, password, recipients=None,
                 fromm=None, subject=None, message=None, msg_type=None):
        self.username = username
        self.password = password
        self.message = message or f"Kindergarten approval {today}"
        self.fromm = fromm or "me"
        self.recipients = recipients.split(',')
        self.subject = subject or f"Kindergarten signed approval for {today}"
        self.msg = MIMEMultipart()
        self.msg['Date'] = formatdate(localtime=True)
        self.msg['Subject'] = self.subject
        msg_type = msg_type or 'plain'
        self.msg.attach(MIMEText(self.message, msg_type))
        self.server = 'smtp.gmail.com'

    def send(self):
        try:
            server = smtplib.SMTP(host=self.server, port='587')
            server.ehlo()
            server.starttls()
            res_auth = server.login(self.username, self.password)
            if not 235 == res_auth[0]:
                raise smtplib.SMTPAuthenticationError
            server.sendmail(from_addr=self.fromm,
                            to_addrs=self.recipients,
                            msg=self.msg.as_string())

            server.close()
        except (AttributeError, TypeError):
            print('Email sending failed')

    def send_mail_with_file(self, filename):
        try:
            ctype, encoding = mimetypes.guess_type(filename)
            if ctype is None or encoding is not None:
                ctype = 'application/octet-stream'
            maintype, subtype = ctype.split('/', 1)
            if maintype == 'text':
                fp = open(filename)
                # Note: we should handle calculating the charset
                msg = MIMEText(fp.read(), _subtype=subtype)
                fp.close()
            elif maintype == 'image':
                fp = open(filename, 'rb')
                msg = MIMEImage(fp.read(), _subtype=subtype)
                fp.close()
            else:
                fp = open(filename, 'rb')
                msg = MIMEBase(maintype, subtype)
                msg.set_payload(fp.read())
                fp.close()
                # Encode the payload using Base64
                encoders.encode_base64(msg)
                # Set the filename parameter
            msg.add_header('Content-Disposition', 'attachment',
                           filename=filename.name)
            self.msg.attach(msg)
        except:
            print('file attachment failed')
        self.send()