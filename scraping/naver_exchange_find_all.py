import requests #url 처리
from bs4 import BeautifulSoup #request 처리

url = "https://finance.naver.com/marketindex/"
response = requests.get(url) #url 응답객체 생성
soup = BeautifulSoup(response.text, 'html.parser') #BeautifulSoup가 일을 해서 html객체 생성

#파일 : find()메서드로 하나씩 찾아봤으니 find_all()매서드로 전체 찾기

#find_all()메서드로 전체 찾기
ul = soup.find('ul', attrs={'class':'data_lst'})
lis = ul.find_all('li') #전체 환율 찾기
for li in lis:
    exchange = li.find('span', attrs={'class':'blind'}) #환율 종류
    value = li.find('span', attrs={'class':'value'}) #환율 지수
    #print(exchange.text, ':', value.text)
    print(exchange.string.split(' ')[-1], ':', value.text) #공백문자로 구분(split()해서 맨 뒤의 문자열 추출