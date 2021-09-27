from urllib import request
from bs4 import BeautifulSoup

target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId-108")

soup=BeautifulSoup(target,"html.parser")

for location in soup.select("location"):
    print("도시:", location.select_one("city").string)
    print("날씨:", location.select_one("wf").string)
    print("최저기온:", location.select_one("tmn").string)
    print("최고기온:", location.select_one("tmx").string)
    print()


from urllib import request
target = request.urlopen("https://google.com")
output = target.read()
print(output)

import shutil
import tempfile
import urllib.request

with urllib.request.urlopen('http://python.org/') as response:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        shutil.copyfileobj(response, tmp_file)

with open(tmp_file.name) as html:
    pass




from urllib import request
from bs4 import BeautifulSoup

url='https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date=20210926'


target=request.urlopen(url)

soup=BeautifulSoup(target,"html.parser")

mov_tit=[]; mov_pt=[]
for line in soup.select('tr'):
    title=line.find('div',class_='tit5')
    if title:
        mov_tit.append(title.get_text())
    point=line.find('td',class_='point')
    if point:
        mov_pt.append(point.text)

for i,(tit,pt) in enumerate(zip(mov_tit,mov_pt)):
    print(i+1,tit, ':', pt)





text='''Yesterday
All my troubles seemed so far away
Now it looks as though they're here to stay
Oh, I believe in yesterday
Suddenly
I'm not half the man I used to be
There's a shadow hanging over me
Oh, yesterday came suddenly
Why she had to go, I don't know
She wouldn't say
I said something wrong
Now I long for yesterday
Yesterday
Love was such an easy game to play
Now I need a place to hide away
Oh, I believe in yesterday
Why she'''
import requests
request_url = "https://openapi.naver.com/v1/papago/n2mt"

headers= {"X-Naver-Client-Id": "nsq8vhhc5S5617N9kYnQ", 
          "X-Naver-Client-Secret":"hgR1oI4QZ7"}
params = {"source": "en", "target": "ko", "text": text}

response = requests.post(request_url, headers=headers, data=params)
print(type(response.text))

result = response.json()
print(result)
print(result['message']['result']['translatedText']) 


while True:
    text=input("번역할 한글 입력>")
    if text=='종료:':
        break
    params = {"source": "en", "target": "ko", "text": text}

    response = requests.post(request_url, headers=headers, data=params)
    result = response.json()
    print(result['message']['result']['translatedText'])


import os
output = os.listdir("./") 
print("os.listdir():",output)
print()

print("#폴더와 파일 구분하기")
for path in output:
    if os.path.isdir(path):
        print("폴더:", path)
    else:
        print("파일:", path)
import os

def read_folder(path):
    output= os.listdir(path)
    for item in output:
        if os.path.isdir(item) :
            read_folder(path+"/"+item)
        else:
            print("파일:",item)
read_folder(input("검색하고자 하는 폴더를 입력"))



def read_folder2(path):
    output = os.listdir(path)
    for item in output:
        if os.path.isdir(path + "\\" + item):
            read_folder2(path + "\\" + item)
        else:
            print("File: ", item)