import smtplib
from email.message import EmailMessage

def send_log_via_email(to_email, log_file_path, sender_email, sender_password):
    msg = EmailMessage()
    msg['Subject'] = 'Automation Toolkit - Rename Log'
    msg['From'] = sender_email
    msg['To'] = to_email
    msg.set_content("Attached is your automation log.")

    with open(log_file_path, 'rb') as f:
        msg.add_attachment(f.read(), maintype='text', subtype='plain', filename=log_file_path.split('/')[-1])

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)
