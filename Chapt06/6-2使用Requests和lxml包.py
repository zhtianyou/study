import requests
from lxml import html
url = "https://www.flag.com.tw/books/school_code_n_algo"
r = requests.get(url)
tree = html.fromstring(r.text)
tag_img = tree.xpath("/html/body/section[2]/table/tr[1]/td[2]/a/img")[0]
print(tag_img)
print(tag_img.tag)
print(tag_img.attrib["src"])

tag_name = tree.xpath("/html/body/section[2]/table/tr[1]/td[2]/a/p")[0]
print(tag_name)
print(tag_name.tag)
print(tag_name.text_content())

#   使用lxml包遍历网页元素
print(tag_img.getparent().tag)
print(tag_img.getnext().tag)
print("-----------------------")
tag_name = tree.xpath("/html/body/section[2]/table/tr[1]/td[2]/a/p")[0]
print(tag_name.tag)
print(tag_name.getprevious().tag)

print("调取兄弟元素，请在父元素a调用getchildren()函数")
for ele in tag_img.getparent().getchildren():
    print(ele.tag)