import imaplib
import email
import logging
from bs4 import BeautifulSoup

from database import save_ticket
from brain import analyze_ticket


logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# -----------------------------
# Email Body Extraction
# -----------------------------
def extract_email_body(msg):
    body = ""

    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))

            # Skip attachments
            if "attachment" in content_disposition:
                continue

            payload = part.get_payload(decode=True)
            if not payload:
                continue

            try:
                text = payload.decode(errors="ignore")
            except:
                continue

            # Prefer plain text
            if content_type == "text/plain":
                return clean_text(text)

            # Fallback to HTML
            if content_type == "text/html" and not body:
                soup = BeautifulSoup(text, "html.parser")
                body = soup.get_text(separator="\n")

    else:
        payload = msg.get_payload(decode=True)
        if payload:
            text = payload.decode(errors="ignore")
            if msg.get_content_type() == "text/html":
                soup = BeautifulSoup(text, "html.parser")
                body = soup.get_text(separator="\n")
            else:
                body = text

    return clean_text(body)


# -----------------------------
# Text Cleaning (خیلی مهم برای ML)
# -----------------------------
def clean_text(text):
    lines = text.splitlines()

    cleaned_lines = []
    for line in lines:
        line = line.strip()

        # remove quoted replies
        if line.startswith(">"):
            continue

        # remove common reply patterns
        if "wrote:" in line.lower():
            break

        cleaned_lines.append(line)

    cleaned_text = "\n".join(cleaned_lines)

    # remove excessive blank lines
    cleaned_text = "\n".join(
        [line for line in cleaned_text.splitlines() if line.strip()]
    )

    return cleaned_text.strip()


# -----------------------------
# Main Processor
# -----------------------------
def process_email(username, password):
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(username, password)
        mail.select("inbox")

        _, message_numbers = mail.search(None, "UNSEEN")

        for num in message_numbers[0].split():
            _, data = mail.fetch(num, "(RFC822)")
            msg = email.message_from_bytes(data[0][1])

            sender = msg.get("from", "Unknown")
            subject = msg.get("subject", "No Subject")

            body = extract_email_body(msg)

            if not body:
                logging.info("Empty email skipped.")
                continue

            sentiment = analyze_ticket(body)

            save_ticket(sender, subject, body, sentiment)

            logging.info(f"Email from {sender} saved with status {sentiment}")

        mail.logout()

    except Exception as e:
        logging.error(f"Error in automation_engine: {e}")


if __name__ == "__main__":
    process_email("amirmahdi.gdrzi12@gmail.com", "noeqsuzwgymwqkgh")