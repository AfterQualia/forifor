# g-inline-text-badges__text
# import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome()
driver.get("https://www.rbc.ru/")
driver.implicitly_wait(10)
needed_text = driver.find_elements(By.CSS_SELECTOR, "[data-vr-headline]" )
for i in needed_text:
    print(i.text)

driver.quit()
# r = requests.get("https://www.rbc.ru/")
# html_in_text = r.text
# soup = BeautifulSoup(html_in_text, 'html.parser')
#print(r.text)

