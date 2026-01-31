import smtplib
from email.message import EmailMessage

main_email = "amirmahdi.gdrzi12@gmail.com"
password = "vggfyjmihpzsterz "

msg = EmailMessage()

msg["Subject"] = "Test Email"
msg["From"] = main_email
msg["To"] = "rexlepyo@gmail.com"

msg.set_content("Hello this is text from code to email")
msg.add_alternative(""""
    <html>
        <body>This is alternative text</body>
        <h1>This is header</h1>
    </html>
    """, subtype="html")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(main_email, password)
    server.send_message(msg)

print('Program finished')