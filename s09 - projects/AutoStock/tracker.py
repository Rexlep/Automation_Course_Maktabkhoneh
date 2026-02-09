import requests
import sqlite3
import schedule
import time
from bs4 import BeautifulSoup


def get_live_price():
    url = "https://milli.gold/?gad_source=1&gad_campaignid=21799795335&gclid=Cj0KCQiAhaHMBhD2ARIsAPAU_D7W27cFJIoPO8zdBbDZpC37uTG1QYrCP7mEeLpbuC-AFHK4DdEtGvcaAmd6EALw_wcB"
    header = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=header)
        soup = BeautifulSoup(response.text, "html.parser")
        price = soup.find("p", attrs={"class": "font-bold text-title1 leading-title1 text-deepOcean-focus md:text-headLine3 md:leading-headLine3 lg:text-headLine2 lg:leading-headLine2"}).text
        price = price.replace("ریال", "")
        print(f"Current Gold price: {price}")

        save_to_db(price)

    except Exception as e:
        print(f"Error occurred: {e}")


def save_to_db(price):
    conn = sqlite3.connect('monitor.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO price_history (price_value) VALUES (?)', (price, ))
    conn.commit()
    conn.close()


schedule.every(50).second.do(get_live_price)

if __name__ == '__main__':
    print("Tracker is running")
    get_live_price()
    while True:
        schedule.run_pending()
        time.sleep(1)