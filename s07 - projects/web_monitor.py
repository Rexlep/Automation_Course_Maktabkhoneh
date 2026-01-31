import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import service
from webdriver_manager.chrome import ChromeDriverManager
from pathlib import Path

url = "https://milli.gold/"
check_selector = 'font-bold'
data_file = 'last_value.txt'

email_sender = 'amirmahdi.gdrzi@gmail.com'
email_password = 'vggfyjmihpzsterz'
email_receiver = 'rexlepyo@gmail.com'


def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(email_sender, email_password)
        server.send_message(msg)


def read_last_value():
    if not Path(data_file).exists():
        return None
    return Path(data_file).read_text(encoding='utf-8')


def save_current_value(value):
    Path(data_file).write_text(value, encoding='utf-8')


def main():
    print("getting driver")
    driver = webdriver.Firefox()
    driver.get(url)
    print("getting url")

    time.sleep(3)

    element = driver.find_element(By.CLASS_NAME, check_selector)
    current_value = element.text.strip()

    last_value = read_last_value()

    if last_value is None:
        save_current_value(current_value)
        print('Initial value saved')

    elif current_value != last_value:
        print('change detected')

        save_current_value(current_value)

        send_email(
            subject='Price changed',
            body=f'The gold price has been changed'

        )
    else:
        print('no change')

    driver.quit()


if __name__ == '__main__':
    main()