from selenium import webdriver
import os
driver = webdriver.Chrome("//Users/youwin/PycharmProjects/chromedriver")
#   html_path = "//Users/youwin/PycharmProjects/study/Chapt07_Selenium/Ch7_4.html"
html_path = "file:///" + os.path.abspath("Ch7_4.html")
driver.implicitly_wait(10)
driver.get(html_path)

#   使用id属性定位网页数据
form = driver.find_element_by_id("loginForm")
print(form.tag_name)
print(form.get_attribute("id"))

#   使用name属性定位网页数据
user = driver.find_element_by_name("username")
print(user.tag_name)
print(user.get_attribute("type"))

eles = driver.find_elements_by_name("continue")
for ele in eles:
    print(ele.get_attribute("type"))

#   使用XPath表达式定位网页数据