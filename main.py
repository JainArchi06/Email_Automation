import smtplib
from email.message import EmailMessage
import csv

# SMTP Configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'Your EmailID'
EMAIL_PASSWORD = 'Your Password'

# Create Email Message
def create_email(subject, body, recipient):
    msg = EmailMessage()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.set_content(body)
    return msg

# Send Email
def send_email(msg):
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print(f"Email sent to {msg['To']}")
    except Exception as e:
        print(f"Failed to send email to {msg['To']}: {e}")

def send_bulk_emails(csv_file, subject, body_template):
    with open(csv_file, newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row if there is one
        for row in reader:
            recipient = row[0]  # Assuming email is the first column
            body = body_template.format(name=row[1])  # Assuming name is the second column
            msg = create_email(subject, body, recipient)
            send_email(msg)
subject = "Exciting Updates from Our Team!"
body_template = "Hello {name},\n\nCould you clarify or expand on what you mean by ? Are you looking for a charming or delightful message, or do you mean something else? Let me know how I can help!\n\nBest regards,\nYour Company"

csv_file = "recipients.csv"
send_bulk_emails(csv_file, subject, body_template)
