#나이 계산 프로그램
"""print("태어난 년도를 입력하세요 : ")
birth_year = input()
print(birth_year)"""

#1)현재 년도, 태어난 년도 선언
current_year = 2021
birth_year = int(input("태어난 년도를 입력하세요 : "))
#2)나이 계산 : 나이 = 현재 년도 - 태어난 년도 +1
age = current_year - birth_year +1
#출력
#print("당신의 나이는", age, "세 입니다"
print("당신의 나이는 " + str(age) + "세 입니다")
