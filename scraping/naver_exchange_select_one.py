import requests #url 처리
from bs4 import BeautifulSoup #request 처리

url = "https://finance.naver.com/marketindex/"
response = requests.get(url) #url 응답객체 생성
soup = BeautifulSoup(response.text, 'html.parser') #BeautifulSoup가 일을 해서 html객체 생성

#먼저 하나를 찾고, 전체를 찾아보자
#찾는 순서(ul class="data_lst" -> li class(blind, value))

#select_one()매서드로 찾기
li = soup.select_one('ul.data_lst li') #태그이름.클래스 이름
#print(li) #찾은 한 개의 li 전체내용 출력
exchange = li.select_one('span.blind')
#print(exchange.text) #출력 : 미국 USD
value = li.select_one('span.value')
#print(value.text) #출력 : 1,186.30
print(exchange.text, ':', value.text) #출력 : 미국 USD : 1,186.40


