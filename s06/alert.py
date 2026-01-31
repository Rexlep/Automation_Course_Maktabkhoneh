import smtplib
from email.message import EmailMessage
import psutil

main_email = "amirmahdi.gdrzi12@gmail.com"
password = "vggfyjmihpzsterz"


def send_alert(message):
    msg = EmailMessage()
    msg['Subject'] = 'Alert From CPU'
    msg['From'] = main_email
    msg['To'] = "rexlepyo@gmail.com"
    msg.set_content(message)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(main_email, password)
        server.send_message(msg)


cpu_percent = psutil.cpu_percent(interval=1)

if cpu_percent > 50:
    send_alert('Alert From CPU\n cpu has more than 50%')
    print('sent email')