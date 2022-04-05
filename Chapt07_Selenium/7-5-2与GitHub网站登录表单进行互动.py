from selenium import webdriver

driver = webdriver.Chrome("//Users/youwin/PycharmProjects/chromedriver")
driver.implicitly_wait(10)
url = "https://github.com/login"
driver.get(url)

username = "zhtianyou"
password = "Ty790413"
user = driver.find_element_by_css_selector("#login_field")
user.send_keys(username)
pwd = driver.find_element_by_css_selector("#password")
pwd.send_keys(password)
button = driver.find_element_by_css_selector(".js-sign-in-button")
button.click()

items = driver.find_elements_by_xpath("//header/div[3]/nav/a")
for item in items:
    print(item.text)
    print(item.get_attribute("href"))
driver.close()