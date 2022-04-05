#   使用requests模块下载图片

import requests

url = "https://bbs.qn.img-space.com/202203/10/408bb5fd1d68e7276f2d42188331004a.jpg"
path = "//Users/youwin/documents/a.jpg"
response = requests.get(url, stream=True)
if response.status_code == 200:
    with open(path, "wb") as fp:
        for chunk in response:
            fp.write(chunk)
        print("图片已经下载")
else:
    print("错误！HTTP请求失败...")

#   使用urllib模块下载图片
import urllib.request
url = "https://bbs.qn.img-space.com/202203/10/408bb5fd1d68e7276f2d42188331004a.jpg"
response = urllib.request.urlopen(url)
fp = open(path, "wb")
size = 0
while True:
    info = response.read(10000)
    if len(info) < 1:
        break
    size = size + len(info)
    fp.write(info)

print(size, "个字符下载...")
fp.close()
response.close()