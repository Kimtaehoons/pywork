import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com/"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser') #html 파싱(해석)할 soup객체 생성

#네이버 메인화면에서 "네이버를 시작페이지로"를 찾을 떄
div = soup.find('div', attrs={'class': 'service_area'}) #div의 class속성을 찾음
first_a = div.find('a') #div속성으로 첫번째 a태그 찾음 
print(first_a)
print(first_a.text)

#네이버 메인화면에서 "쥬니어네이버"를 찾을 때
all_a = div.find_all('a')
print(all_a)
print(all_a[1].text)
