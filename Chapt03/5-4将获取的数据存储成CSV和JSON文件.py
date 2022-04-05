import csv
import requests
from bs4 import BeautifulSoup
print("----------------读取CSV文件----------------")
csvfile = "//Users/youwin/documents/Example.csv"
with open(csvfile, "r") as fp:
    reader = csv.reader(fp)
    for row in reader:
        print(','.join(row))

print("----------------将数据写入CSV文件----------------")
csvfile = "//Users/youwin/documents/Example2.csv"
list1 = [[10, 33, 45], [5,25,56]]
with open(csvfile, "w+", newline='') as fp:
    writer = csv.writer(fp)
    writer.writerow(["Data1","Data2","Data3"])
    for row in list1:
        writer.writerow(row)

print("----------------从W3Shool网站获取表格数据写入CSV文件----------------")
url = "https://www.w3school.com.cn/html/html_media.asp"
csvfile = "//Users/youwin/documents/VideoFormat.csv"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
tag_table = soup.find(class_="dataintable")     #   找到<table>
rows = tag_table.findAll("tr")
with open(csvfile, 'w+', newline='', encoding="utf-8") as fp:
    writer = csv.writer(fp)
    for row in rows:
        rowList = []
        for cell in row.findAll(["td", "th"]):
            rowList.append(cell.get_text() .replace("\n", "") .replace("\r", ""))
        writer.writerow(rowList)
