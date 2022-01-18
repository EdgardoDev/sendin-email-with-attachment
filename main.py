from dotenv import load_dotenv
import yagmail
import os

load_dotenv()

# Create initial variables.
sender_email = os.getenv("SENDER_EMAIL")
receiver_email = os.getenv("RECEIVER_EMAIL")

# Email subject.
email_subject = "Hello from Python!"

# Email body. Here to be able to send the attachment the contents of the email body
# has been transformed into a list, that way the attachment has been added to the list
# as an extra list item.
email_body = ["""
Hello! 
This is the body content of the email.
Best regards,
The Python Script.
""", "contacts.csv"]

# Create an SMTP object instance
smtp = yagmail.SMTP(user=sender_email, password=os.getenv("APP_PASSWORD"))
# Send email.
smtp.send(to=receiver_email, subject=email_subject, contents=email_body)

print("Email successfully sent!")