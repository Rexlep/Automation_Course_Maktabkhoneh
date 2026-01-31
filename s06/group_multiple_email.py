import smtplib
from email.message import EmailMessage

main_email = "amirmahdi.gdrzi12@gmail.com"
password = "vggfyjmihpzsterz"

msg = EmailMessage()

msg['Subject'] = 'Group Email'
msg['From'] = main_email
msg['To'] = ['rexlepyo@gmail.com', 'testerrar59@gmail.com']

msg.set_content('Hello World')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login(main_email, password)
    server.send_message(msg)

print("Email sent")