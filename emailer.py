import smtplib
from email.message import EmailMessage

def send_email():
    email = EmailMessage()
    email['from'] = 'you@gmail.com'
    email['to'] = 'target@gmail.com'
    email['subject'] = 'Aura says hello'
    email.set_content("This is a test from Aura.")
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('you@gmail.com', 'your_app_password')
        smtp.send_message(email)