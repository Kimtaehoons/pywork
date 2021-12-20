import requests #url 처리
from bs4 import BeautifulSoup #request 처리

url = "https://finance.naver.com/marketindex/"
response = requests.get(url) #url 응답객체 생성
soup = BeautifulSoup(response.text, 'html.parser') #BeautifulSoup가 일을 해서 html객체 생성

#파일 : select_one()메서드로 하나씩 찾아봤으니 select()매서드로 전체 찾기

#select()매서드로 전체 찾기
lis = soup.select('div.market1 ul li')
# print(lis)
for li in lis:
    exchange = li.select_one('span.blind') #환율 종류
    value = li.select_one('span.value') #환율 지수
    #print(exchange.text, ':', value.text)
    print(exchange.string.split(' ')[-1], ':', value.text) #공백문자로 구분(split()해서 맨 뒤의 문자열 추출