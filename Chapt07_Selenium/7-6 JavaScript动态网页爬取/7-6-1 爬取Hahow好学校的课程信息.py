from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome("//Users/youwin/PycharmProjects/chromedriver")
driver.implicitly_wait(10)
url = "https://hahow.in/courses"
driver.get(url)

items = driver.find_elements_by_css_selector(".marg-b-10")
for item in items:
    print(item.text)
driver.close()