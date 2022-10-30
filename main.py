
from bs4 import BeautifulSoup
import requests

url = "https://sistemas.unmsm.edu.pe/site/index.php"
r = requests.get(url, verify=False)

html_doc = r.text

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.find_all('div', 'mfp_carousel_item', 'tns-item')[15].div.h4.a.string) # <-- Get title of news number 15
print(soup.find_all('div', 'mfp_carousel_item', 'tns-item')[15].div.p.string) # <-- Get description of news number 15


