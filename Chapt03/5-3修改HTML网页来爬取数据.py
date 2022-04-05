from bs4 import BeautifulSoup

#   更改HTML标签名称和属性
print("--------更改HTML标签名称和属性---------")
soup = BeautifulSoup("<b class='score'>Job</b>", "lxml")
tag = soup.b
tag.name = "p"
tag["class"] = "question"
tag["id"] = "name"
print(tag)
del tag["class"]
print(tag)

#   修改HTML标签的文字内容
print("--------修改HTML标签的文字内容---------")
tag.string = "Mary"
print(tag)

#   新增HTML标签和文字内容
print("--------新增HTML标签和文字内容---------")
tag.append("Joe")
print(tag)
new_str = NavigableString("Chen")
tag.append(new_str)
print(tag)