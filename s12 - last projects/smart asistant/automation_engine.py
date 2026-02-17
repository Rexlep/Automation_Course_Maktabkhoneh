import imaplib
import email
import logging
from database import save_ticket
from brain import analyze_ticket

logging.basicConfig(filename="automation.log",level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")


def process_email(username, password):
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(username, password)
        mail.select("inbox")

        _, message = mail.search(None, "UNSEEN")

        for num in message[0].split():
            _, data  = mail.fetch(num, "(RFC822)")
            msg = email.message_from_bytes(data[0][1])

            sender = msg["from"]
            subject = msg['subject']
            body = ""

            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.get_playload(decode=True).decode()

            else:
                body = msg.get_playload(decode=True).decode()

            sentiment = analyze_ticket(body)
            save_ticket(sender, subject, body, sentiment)

            logging.info(f"Email from {sender} with this status {sentiment}")

        mail.logout()

    except Exception as e:
        logging.error(f"Error in automation_engine; {e}")


if __name__ == "__main__":
    process_email("amirmahdi.gdrzi12@gmail.com", "noeqsuzwgymwqkgh")