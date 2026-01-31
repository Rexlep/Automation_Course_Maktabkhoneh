import smtplib
from email.message import EmailMessage
from pathlib import Path

main_email = "amirmahdi.gdrzi12@gmail.com"
password = "vggfyjmihpzsterz"

msg = EmailMessage()

msg["Subject"] = "Test Email"
msg["From"] = main_email
msg["To"] = "rexlepyo@gmail.com"

file_path = Path('data.csv')

with open(file_path, 'rb') as f:
    msg.add_attachment(
        f.read(),
        maintype='application',
        subtype='octet-stream',
        filename=file_path.name
    )


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login(main_email, password)
    server.send_message(msg)


print("Email sent")