import requests
from bs4 import BeautifulSoup

#원하는 내용 특정 한 가지만 가져올 때
def getcontent():
    url = "https://finance.naver.com/item/main.naver?code=005930" #주식 종목 html내용 가져오기 함수
    response = requests.get(url)
    content = BeautifulSoup(response.text, 'html.parser')
    return content

content = getcontent()
today = content.find('div', attrs={'class':'today'}) #네이버 삼성전자 주가 부분 가져오기
#print(today)
price = today.find('span', attrs={'class':'blind'}) #위에까지만 가도 장 마감 후엔 주가부분으로 바로 가는데 장중이라 해당 자료가 변동이 생서 blind가 생성되므로 재설정
#print(price)
print("삼성전자 주가 : {}원".format(price.text))

