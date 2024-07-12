import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SendMail:
    def __init__(self, EMAIL, EMAIL_PASSWORD) -> None:
        self._EMAIL = EMAIL
        self._EMAIL_PASSWORD = EMAIL_PASSWORD


    def send_email(self, from_email, to_email, subject, message, smtp_server, smtp_ssl_port, html=False):
        '''
        UseCase:
        ---
        Send Email via SMTP, Here MIMEMultipart() and MIMEText is used to make this function dynamic so it can also send HTML (with CSS, JS) content. Also can send Plain Text.

        Args:
        ---
        - from_email: str -> Sender Email
        - to_email: str -> Where to send Email.
        - subjet: str -> Subject of the Email.
        - message: str -> Plain Text or HTML in str.
        - *host_and_port -> tuple with host name such as smtp.gmail.com and the SSL port such as 465.
        - html: bool (default False) -> True when message is HTML  

        '''
        try:
            # Email Content and setting its attribute.
            msg = MIMEMultipart()
            msg['From'] = from_email
            msg['To'] = to_email
            msg['Subject'] = subject

            html_or_plain = 'html' if html else 'plain'
            msg.attach(MIMEText(message, html_or_plain))
            
            # Server Login and Sending Mail through SMTP SSL, then quit.
            mailserver = smtplib.SMTP_SSL(smtp_server, smtp_ssl_port)        
            mailserver.ehlo()
            mailserver.login(self._EMAIL, self._EMAIL_PASSWORD) 
            mailserver.sendmail(from_email, to_email, msg.as_string())
            mailserver.quit()

            print(f"Successfully sent email to -> {to_email}")

        except Exception as e:
            print(f"Failed to send email to -> {to_email}: {e}")
