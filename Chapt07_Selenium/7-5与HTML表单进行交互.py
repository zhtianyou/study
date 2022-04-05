from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("//Users/youwin/PycharmProjects/chromedriver")
driver.implicitly_wait(10)
url = "https://cn.bing.com"
driver.get(url)

keyword = driver.find_element_by_xpath("//input[@id='sb_form_q']")
keyword.send_keys("Xpath")
keyword.send_keys(Keys.ENTER)

items = driver.find_elements_by_xpath("//li[@class='b_algo']")

for item in items:
    a = item.find_element_by_tag_name("a")
    print(a.get_attribute("href"))
    print(a.text)

driver.quit()