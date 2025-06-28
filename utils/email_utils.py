import smtplib
from email.message import EmailMessage
import os

def send_log_via_email(to_email, log_file_path, sender_email, sender_password):
    if not os.path.exists(log_file_path):
        raise FileNotFoundError(f"Log file not found: {log_file_path}")

    msg = EmailMessage()
    msg['Subject'] = '📄 Automation Toolkit - Log File'
    msg['From'] = sender_email
    msg['To'] = to_email
    msg.set_content("Hi,\n\nAttached is your automation log file.\n\nRegards,\nAutomation Toolkit")

    with open(log_file_path, 'rb') as f:
        file_data = f.read()
        file_name = os.path.basename(log_file_path)
        msg.add_attachment(file_data, maintype='text', subtype='plain', filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)
