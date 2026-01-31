import smtplib
from email.message import EmailMessage

main_email = "amirmahdi.gdrzi12@gmail.com"
password = "vggfyjmihpzsterz"

msg = EmailMessage()

msg["Subject"] = "Test Email"
msg["From"] = main_email
msg["To"] = "rexlepyo@gmail.com"

html = """
<h2 style="color:green;">Automation report</h2>
<p>Status : <b> Success </b></p>
<button  style="color:white;background-color:#696969; width:80px;height:20px;shadow:none;corner-radius:10px;">View Detail</button>
"""

msg.add_alternative(html, subtype='html')

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(main_email, password)
    server.send_message(msg)


print("The email has been sent successfully")