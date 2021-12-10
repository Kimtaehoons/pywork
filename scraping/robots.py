import requests #url 접속 및 정보 가져오는 모듈로 cmd창에서 pip install requests입력
#로봇 배제 표준 내역 가져오기
url = "https://www.naver.com/robots.txt"

response = requests.get(url) #url을 요청해서 응답 객체 생성
print(response) #처리결과 확인(200 - 응답 성공, 404 - 응답 실패)
print(response.text) #txt의 내용 보이기

response2 = requests.get("http://www.python.org/robots.txt")
print(response2)
print(response2.text) #문자열만 출력