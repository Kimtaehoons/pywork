import requests
from bs4 import BeautifulSoup

#getprice()함수와 get방식 검색('?')을 활용(item_code매개변수 사용)한 주가확인 틀 만들기
def getcontent(item_code):
    url = "https://finance.naver.com/item/main.naver?code=" + item_code
    response = requests.get(url)
    content = BeautifulSoup(response.text, 'html.parser')
    return content

def getprice(item_code):
    content = getcontent(item_code)
    today = content.find('div', attrs={'class':'today'})
    price = today.find('span', attrs={'class':'blind'})
    return price

#함수 호출(원하는 기업의 item_code 가져오기)
삼성전자 = getprice('005930')
네이버 = getprice('035420')
카카오 = getprice('035720')

print("삼성전자 주가 : {}원".format(삼성전자.text))
print("네이버 주가 : {}원".format(네이버.text))
print("카카오 주가 : {}원".format(카카오.text))

