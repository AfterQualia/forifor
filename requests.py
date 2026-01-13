import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.rbc.ru/")
print(r.text)
# g-inline-text-badges__text