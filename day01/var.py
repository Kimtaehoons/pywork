#변수 사용하기 - 주석 #(한줄), """ 또는 ''' 감싸준다(여러줄) 문자는 "", '')
print('***회원가입***')
userid = 'hangul'
userpw = 'han1234'
name = '한글'
phone = '010-0000-0000'
age = 25

#문자 출력 - ,(연결, 공백) 연산자 사용
"""
print("아이디 :", userid)
print("비밀번호 :", userpw)
print("이름 :", name)
print("전화번호 :", phone)
print("나이 :", age)
"""

#문자 출력 - +(연결) 연산자 사용
print("="*30)
print("아이디 : " + userid)
print("비밀번호 : " + userpw)
print("이름 : " + name)
print("전화번호 : " + phone)
print("나이 :" + str(age))
#자동 형변환은(문자>숫자, 문자를 따라가므로) 오류, 출력할 때는 용량이 큰 문자로 형변환을 맞춰준다. 숫자는 문자 자료형으로 형변환 str()함수 사용
print("="*30)




