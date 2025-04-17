import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = "localhost"
smtp_port = 1025

sender = "sender@example.com"
recipient = "recipient@example.com"
subject = "Hello from the client"
body = "This is a test message sent to a local SMTP server."

msg = MIMEMultipart()
msg["From"] = sender
msg["To"] = recipient
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain"))

print("🔌 Connecting to SMTP server...")
with smtplib.SMTP(smtp_server, smtp_port) as server:
    # Enable debugging to print all the SMTP commands and responses
    server.set_debuglevel(1)

    # These are the actual SMTP commands/responses
    server.ehlo()
    server.sendmail(sender, recipient, msg.as_string())
    print("✅ Email sent.")
