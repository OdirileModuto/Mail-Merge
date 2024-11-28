import csv
import smtplib
from email.mime.text import MIMEText

# SMTP configuration
smtp_server = 'smtp.yourserver.com'
sender_email = 'your_email@example.com'
sender_password = 'your_password'

# Read the CSV file
with open('contacts.csv', mode='r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        # Prepare the email content
        subject = f'Hello {row["name"]}'
        body = f'Hi {row["name"]},\nYour score is {row["score"]}.'
        
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = row['email']
        
        # Send the email
        with smtplib.SMTP(smtp_server) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)

print("Emails sent successfully!")