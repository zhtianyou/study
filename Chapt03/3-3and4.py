
from bs4 import BeautifulSoup

with open("//Users/youwin/documents/Example.html", "r", encoding="utf-8") as fp:
    soup = BeautifulSoup(fp, "lxml")
tag_p = soup.find(name="p")
tag_a = tag_p.find(name="a")
tag_div = soup.find(id = "q2")
tag_a = tag_div.find("a")

print(tag_a.string)

tag_li = soup.find(attrs={"class":"response"})
tag_span = tag_li.find("span")
print(tag_span.string)

tag_div = soup.find(id="q2")
tag_li = tag_div.find(class_="response")
tag_span = tag_li.find("span")
print(tag_span.string)

tag_div = soup.find(attrs={"data-custom":"important"})
print(tag_div.string)

tag_str = soup.find(text="请问你的性别?")
print(tag_str)
tag_str = soup.find(text="10")
print(tag_str)
print(type(tag_str))
print(tag_str.parent.name)
tag_str = soup.find(text="男-")
print(tag_str)

# 使用多个条件搜索HTML标签

tag_div = soup.find("div", class_="question")
print(tag_div)
tag_p = soup.find("p", class_="question")
print(tag_p)

#   使用Python函数定义搜索条件
def is_secondary_question(tag):
    return tag.has_attr("href") and \
           tag.get("href") == "http://example.com/q2"
tag_a = soup.find(is_secondary_question)
print(tag_a)

tag_list = soup.find_all("p", class_="question", limit=2)
print(tag_list)
for question in tag_list:
    print(question.a.string)

#   搜索所有标签
tag_div = soup.find("div", id="q2")
tag_all = tag_div.find_all(True)
print(tag_all)

#   没有使用递归（recursive）来执行搜索

tag_div = soup.find("div", id="q2")
#   找出所有<li>子孙标签
tag_list = tag_div.find_all("li")
print(tag_list)
tag_list = tag_div.find_all("li", recursive=False)
print(tag_list)
