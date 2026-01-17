import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(subject: str, body: str) -> None:
    sender_email = os.getenv("SMTP_EMAIL")
    sender_password = os.getenv("SMTP_PASSWORD")

    print(f"DEBUG: SMTP_EMAIL is {'set' if sender_email else 'NOT set'}")
    print(f"DEBUG: SMTP_PASSWORD is {'set' if sender_password else 'NOT set'}")
    
    if sender_email:
        print(f"DEBUG: Email will be sent to: {sender_email}")
    
    if not sender_email or not sender_password:
        raise ValueError("SMTP credentials not found in environment variables")
    
    receiver_email = sender_email

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    try:
        print("DEBUG: Connecting to Gmail SMTP server...")
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        print("DEBUG: Logging in...")
        server.login(sender_email, sender_password)
        print("DEBUG: Sending email...")
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()

        print("Email sent successfully.")

    except Exception as e:
        print(f"Failed to send email: {e}")
        print(f"DEBUG: Error type: {type(e).__name__}")
        raise
