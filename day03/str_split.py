#문자열 함수 - 특별한 1차원 리스트
s = "banana, grape, apple"
x = s.split(',') #콤마(,) 구분기호로 설정
print(x)

s2 = "a:b:c:d"
y = s2.split(':')
print(y)
print(s2[-1])
print(s2[1:])

#두 수를 동시에 입력 받아 더하기
#차례대로
"""
n1 = int(input("수1 입력 :")) #숫자는 int로 덮어준다
n2 = int(input("수2 입력 :"))
add = n1 + n2
print(add)
"""

n1, n2 = input("두 수 입력 :").split() #문자이므로 int빼준다, 문자니까 공백으로 끊어준 것
add = int(n1) + int(n2) #숫자로 변환돼야 하므로 int로 덮어준다
print(add)