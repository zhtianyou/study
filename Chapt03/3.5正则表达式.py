import re
from bs4 import BeautifulSoup

with open("//Users/youwin/documents/Example.html", "r", encoding="utf-8") as fp:
    soup = BeautifulSoup(fp, "lxml")
regexp = re.compile("男-")
tag_str = soup.find(text=regexp)
print(tag_str)
regexp = re.compile("\w+-")
tag_list = soup.find_all(text=regexp)
print(tag_list)