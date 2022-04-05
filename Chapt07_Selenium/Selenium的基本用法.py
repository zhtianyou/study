from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome("//Users/youwin/PycharmProjects/study/chromedriver")
driver.implicitly_wait(10)
driver.get("http://example.com")
#   使用Selenium定位网页数据
h1 = driver.find_element_by_tag_name("h1")
print(h1.text)
p = driver.find_element_by_tag_name("p")
print(p.text)
driver.close()


"""
#   解析存储成HTML网页文件
soup = BeautifulSoup(driver.page_source, "lxml")
fp = open("index.html", "w", encoding="utf-8")
fp.write(soup.prettify())
print("写入文件index.html......")
fp.close()
driver.close()
"""
