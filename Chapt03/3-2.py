from bs4 import BeautifulSoup
import requests

"""
r = requests.get("http://example.com")
r.encoding = "utf-8"
soup = BeautifulSoup(r.text, "lxml")
print(soup)
"""

"""
with open("//Users//youwin//text.txt", "r", encoding="utf-8") as fp:
    soup = BeautifulSoup(fp, "lxml")
    print(soup.prettify())
"""

"""
r =requests.get("http://example.com")
r.encoding ="utf-8"

soup = BeautifulSoup(r.text, "lxml")

fp = open("//Users//youwin//test2.txt", "w", encoding="utf-8")
fp.write(soup.prettify())
print("写入文件test.txt...")
fp.close()
"""

html_str = "<div id='msg' class='body strikeout'> <p> Final Test </p> Hello World! </div>"
soup = BeautifulSoup(html_str, "lxml")
tag = soup.div
comment = soup.p.string
print(type(tag))
print(tag.name)
print(tag["id"])
print(tag["class"])
print(tag.attrs)
print(tag.string)
print(type(tag.string))
print(tag.text)
print(type(tag.text))
print(tag.get_text())
print(tag.get_text("-"))
print(tag.get_text("-", strip=True))
print(soup.name)
print(comment)
print(type(comment))

html = " <p><!-- 注释文字 --></p> "
hs = BeautifulSoup(html, "lxml")
comment = hs.p.string
print(comment)
print(type(comment))
