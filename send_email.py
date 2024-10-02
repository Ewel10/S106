import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email():
    email_user = os.environ.get('EMAIL_USER') 
    email_password = os.environ.get('EMAIL_PASSWORD') 
    email_to = os.environ.get('EMAIL_TO') 
    subject = 'Notificação do Pipeline'
    body = 'Pipeline executado com sucesso!'
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, email_password)
    text = msg.as_string()
    server.sendmail(email_user, email_to, text)
    server.quit()

if __name__ == "__main__":
    send_email()
