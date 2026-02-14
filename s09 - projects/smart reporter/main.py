import os
import sqlite3
import pandas as pd
import shutil
import smtplib
import config
from email.message import EmailMessage


def init_db():
    conn = sqlite3.connect(config.DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS sales_history (
                        product TEXT,
                        price REAL,
                        date TEXT)
    """)

    conn.close()


def process_and_report():
    if not os.path.exists(config.INBOX_DIR):
        os.mkdir(config.INBOX_DIR)
    files = [f for f in os.listdir(config.INBOX_DIR) if f.endswith(".csv")]

    if not files:
        print("No files found")
        return

    all_dfs = []
    for file in files:
        path = os.path.join(config.INBOX_DIR, file)
        df = pd.read_csv(path)
        all_dfs.append(df)

    combined_df = pd.concat(all_dfs, ignore_index=True)
    total_sale = combined_df['price'].sum()

    conn = sqlite3.connect(config.DB_NAME)
    combined_df.to_sql('sales_history', conn, if_exists='append', index=False)
    conn.close()

    if not os.path.exists(config.ARCHIVE_DIR): os.mkdir(config.ARCHIVE_DIR)
    for file in files:
        shutil.move(os.path.join(config.INBOX_DIR, file), os.path.join(config.ARCHIVE_DIR, file))

    send_email(total_sale)


def send_email(total_sale):
    msg = EmailMessage()
    msg['Subject'] = 'Sales History'
    msg['From'] = config.EMAIL_ADDRESS
    msg['To'] = config.RECEIVER_EMAIL
    msg.set_content(f"Total sale: {total_sale}")

    try:
        with smtplib.SMTP_SSL(config.SMTP_HOST, config.SMTP_PORT) as server:
            server.login(config.EMAIL_ADDRESS, config.EMAIL_PASSWORD)
            server.send_message(msg)
        print("Email sent")

    except Exception as e:
        print(f"Error {e}")


if __name__ == "__main__":
    init_db()
    process_and_report()