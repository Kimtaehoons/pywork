import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser') #resp.text로 생략하지 않도록 주의

#본문 이미지 경로 출력
target_img = soup.find('img', attrs={'alt':'Seoul-metro-2009-20180916-103548.jpg'})
print("이미지 경로(전체) : ", target_img)

#파일 입출력을 통해 경로에 있는 이미지 복사해서 파일 저장
target_img_src = target_img.get('src') #이미지 소스파일 가져오기
print("이미지 경로(src) : ", target_img_src)

#이미지 경로(url) 요청
target_img_resp = requests.get("http:" + target_img_src)
print(target_img_resp)

#파이너리 파일 쓰기
with open("./output/subway_train.jpg", 'wb') as f: #이미지 넣을 위치 설정
    f.write(target_img_resp.content) #이미지는 content속성 사용