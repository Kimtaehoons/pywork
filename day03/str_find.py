#find함수 - 문자의 위치(인덱스 번호)를 찾는 함수
s = "Hello, welcome to my website!"
print(s.find('H')) #0번 위치
print(s.find('ll')) #첫 번째 문자 위치
print(s.find('k')) #찾는 문자 없을 땐, -1값이 출력
s = s.find("welcome") #단어로 검색해 첫 문자 위치를 찾음, s에 다시 변수값을 담음
print(s)

#strip함수 - 공백 제거
str1 = " hi, soo!"
print(str1.strip())
print(str1.lstrip())

txt = "       banana       "
x = txt.strip()
print("Of all fruits", x, "is my favorite")

#isnumeric함수 - 숫자인지 검사하는 함수
text = "123".isnumeric()
print(text)
text1 = "123ab".isnumeric()
print(text1)
