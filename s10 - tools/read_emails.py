import imaplib
import email
from email.header import decode_header

user_name = "amirmahdi.gdrzi12@gmail.com"
app_password = "noeqsuzwgymwqkgh"

mail = imaplib.IMAP4_SSL('imap.gmail.com')

mail.login(user_name, app_password)
mail.select('inbox')

status, message = mail.search(None, "All")
email_ids = message[0].split()

last_email_id = email_ids[-1]

status, data = mail.fetch(last_email_id, "(RFC822)")

for response_part in data:
    if isinstance(response_part, tuple):
        msg = email.message_from_bytes(response_part[1])

        subject, encoding = decode_header(msg['Subject'])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding if encoding else "utf-8")

        print(f"Subject :{subject}")
        print(f"From: {msg.get("From")}")


mail.logout()
