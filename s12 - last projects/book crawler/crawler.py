import requests
import sqlite3
from bs4 import BeautifulSoup
from transformers import pipeline

# Load AI model
analyzer = pipeline("sentiment-analysis")


def scrape_and_analyse():
    url = "https://books.toscrape.com/catalogue/category/books/science_22/index.html"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    books_data = soup.select(".product_pod")

    # Connect once before the loop
    conn = sqlite3.connect("market_watcher.db")
    cursor = conn.cursor()

    for book in books_data:
        title = book.h3.a['title']

        # FIX 1: Clean price string properly using replace or slicing
        price_text = book.select_one(".price_color").text
        # We remove both 'Â' and '£' symbols
        clean_price = price_text.replace("Â", "").replace("£", "")
        price = float(clean_price)

        availability = book.select_one('.instock.availability').text.strip()

        # AI Analysis
        ai_result = analyzer(title)[0]
        sentiment = ai_result['label']

        cursor.execute("INSERT INTO books (title, price, availability, sentiment) VALUES (?, ?, ?, ?)",
                       (title, price, availability, sentiment))

        conn.commit()

    conn.close()
    print("Scraping and analysis finished. Data saved to Database")


if __name__ == "__main__":
    scrape_and_analyse()