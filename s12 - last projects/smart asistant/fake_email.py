import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time


def send_mock_emails(email_address, app_password):
    """
    Sends multiple test emails to simulate real customer behavior.
    """
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    test_scenarios = [
        {
            "subject": "URGENT: System Crash",
            "body": "I am extremely frustrated. Your software crashed my computer twice today!"
        },
        {
            "subject": "Quick Question",
            "body": "Hello, do you provide any student discounts for the annual plan? Regards."
        },
        {
            "subject": "Great Experience",
            "body": "I just wanted to say thank you! Your automation tools saved me 10 hours this week."
        },
        {
            "subject": "Feature Request",
            "body": "It would be great if you could add a dark mode to the dashboard."
        },
        {
            "subject": "Refund Request",
            "body": "The tool doesn't meet my needs. I want a full refund immediately."
        }
    ]

    try:
        print("Connecting to server...")
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email_address, app_password)

        for i, scenario in enumerate(test_scenarios, 1):
            msg = MIMEMultipart()
            msg['From'] = email_address
            msg['To'] = "amirmahdi.gdrzi12@gmail.com"  # Sending to yourself for testing
            msg['Subject'] = scenario['subject']

            msg.attach(MIMEText(scenario['body'], 'plain'))

            server.send_message(msg)
            print(f"[{i}/{len(test_scenarios)}] Sent: {scenario['subject']}")

            time.sleep(1)

        server.quit()
        print("\nSuccess: All test emails have been sent to your Inbox.")

    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    USER_EMAIL = "rexlepyo@gmail.com"
    APP_PASSWORD = "etjvxkwiaxwjamqw"

    send_mock_emails(USER_EMAIL, APP_PASSWORD)