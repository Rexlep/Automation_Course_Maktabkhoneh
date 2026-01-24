from bs4 import BeautifulSoup

html_doc = """
    <html>  
        <body>
            <h1>Hello World!</h1>
            <p class="intro">First Paragraph</p>
            <p class="intro">Second Paragraph </p>
            <p id="special">Third Paragraph Special</p>
            <a href="http://python.org" class="link", id="test" style="color:#696969;">First Link</a>
            <a href="http://python.org" class="link">Second Link</a> 
        </body
    </html>
"""

soup = BeautifulSoup(html_doc, "html.parser")
paragraph = soup.find_all("p")

# print(paragraph[0].text)


# find method in BS
first_paragraph = soup.find("p")
print(first_paragraph)

first_intro = soup.find(class_="intro")
print(first_intro)

first_link = soup.find("a")
print(first_link["href"])
print(first_link.attrs)
print(first_link)

if "class" in first_link.attrs:
    print(first_link.attrs["class"])

special_item = soup.find("p", id="special")
print(special_item.text)