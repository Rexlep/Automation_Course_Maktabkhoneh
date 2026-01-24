from bs4 import BeautifulSoup

html_doc = """
    <html>  
        <body>
            <div>
                <h1>Hello World!</h1>
                <p class="intro">First Paragraph</p>
                <p class="intro">Second Paragraph </p>
                <p id="special">Third Paragraph Special</p>
                <a href="http://python.org" class="link">First Link</a>
                <a href="http://python.org" class="link">Second Link</a>
            </div>
        </body
    </html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

all_paragraphs = soup.select('p')
print(all_paragraphs)

class_element = soup.select(".intro")
print(class_element)

special_item = soup.select("#special")
print(special_item)

div_p = soup.select("div p")
print(div_p)

headers_links = soup.select("h1, a")
print(headers_links)