from bs4 import BeautifulSoup

file = "//Users/youwin/documents/Example.html"

with open(file, "r", encoding="utf-8") as fp:
    soup = BeautifulSoup(fp, "lxml")

#   找出指定CSS选择器字符串和标签名称
print("↓    ↓   ↓   ↓   ↓   找出指定CSS选择器字符串和标签名称  ↓    ↓   ↓   ↓   ↓")
tag_item = soup.select("#q1 > ul > li:nth-of-type(1) > span")
print(tag_item[0].string)
tag_title = soup.select("title")
print(tag_title[0].string)
tag_first_div = soup.find("div")
tag_div = tag_first_div.select("div:nth-of-type(3)")
print(tag_div[0])

#   找出指定标签下的特定子孙标签
print("↓    ↓   ↓   ↓   ↓   找出指定标签下的特定子孙标签  ↓    ↓   ↓   ↓   ↓")
tag_title = soup.select("html head title")
print(tag_title[0].string)
tag_a = soup.select("body div a")
print(tag_a)

#   找出特定标签下的直接子孙标签
print("↓    ↓   ↓   ↓   ↓   找出特定标签下的直接子孙标签  ↓    ↓   ↓   ↓   ↓")
tag_a = soup.select("p > a")
print(tag_a)
tag_li = soup.select("ul > li:nth-of-type(2)")
print(tag_li)
tag_span = soup.select("div > #email")
print(tag_span)

#   找出兄弟标签
print("↓    ↓   ↓   ↓   ↓   找出兄弟标签  ↓    ↓   ↓   ↓   ↓")
tag_div = soup.find(id="q1")
print(tag_div.p.a.string)
print("--------搜索之后的所有兄弟标签---------")
tag_div = soup.select("#q1 ~ .survey")
for item in tag_div:
    print(item.p.a.string)
print("--------搜索下一个兄弟标签---------")
tag_div = soup.select("#q1 + .survey")
for item in tag_div:
    print(item.p.a.string)

#   找出class和id属性值的标签
print("--------找出class和id属性值的标签---------")
tag_div = soup.select("#q1")
print(tag_div[0].p.a.string)
tag_span = soup.select("span#email")
print(tag_span[0].string)
tag_div = soup.select("#q1, #q2")   #多个id属性
for item in tag_div:
    print(item.p.a.string)
print("-----------------")
tag_div = soup.find("div")
tag_p = tag_div.select(".question")
for item in tag_p:
    print(item.a["href"])
tag_li = soup.select("[class~=selected]")
for item in tag_li:
    print(item)

