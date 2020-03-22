from bs4 import BeautifulSoup
import pandas as pd
import codecs


html_doc = codecs.open("whatsapptest.htm", 'r', 'utf-8')
soup = BeautifulSoup(html_doc, 'html.parser')


selector = 'span._3NWy8 > *'


found = soup.select(selector)

# Extract data from the found elements
data = [x.text.split(';')[-1].strip() for x in found]

for x in data:
    print(x)