import csv
import time
import smtplib
from email.message import EmailMessage

main_email = "amirmahdi.gdrzi12@gmail.com"
password = "vggfyjmihpzsterz"

with open('emails.csv') as f:
    reader = csv.reader(f)
    recipients = [row[0] for row in reader]

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login(main_email, password)

    for email in recipients:
        msg = EmailMessage()
        msg['Subject'] = 'Automation with python - Bulk emails'
        msg['From'] = main_email
        msg['To'] = email
        msg.set_content("Hello this is test from this email")

        server.send_message(msg)
        time.sleep(2)


print("Email sent")