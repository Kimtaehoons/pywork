#if~elif~else문
#놀이공원 입장료 계산 프로그램

age = 8
if age < 8:
    print("미취학 아동입니다")
    charge = 1000
elif age >= 8 and age < 14:
    print("초등학생입니다")
    charge = 2000
elif age >= 14 and age < 20:
    print("초등학생입니다")
    charge = 2500
else:
    print("일반입입니다")
    charge = 3000
print("입장료는 " + str(charge) + "원 입니다")
