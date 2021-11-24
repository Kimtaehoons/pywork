"""
name = input('이름을 입력하세요 : ')
height = float(input('키(cm)를 입력하세요 : ')) * 100
weight = float(input('몸무게를 입력하세요 : '))

bmi = float(weight) / float(height * height) * 100

print(str("{}".format(name)) + "님의 bmi는" + str("{}".format(bmi)) + "입니다.")

if bmi < 20:
    print("저체중입니다")
elif bmi >= 20 and bmi <= 24:
    print("정상입니다")
elif bmi >= 25 and bmi <= 29:
    print("과체중입니다")
else:
    print("비만입니다")
"""

name = input('이름을 입력하세요 : ')
height = float(input('키(cm)를 입력하세요 : '))
height = height / 100 #height를 입력하면 m로 입력된다. 그래서 cm로 환산
weight = float(input('몸무게를 입력하세요 : '))

bmi = weight / (height * height)

print("{}님의 bmi는 {:.1f}입니다.".format(name, bmi)) #.1f는 소수 첫째자리까지를 출력
print("%s님의 bmi는 %.1f입니다." % (name, bmi)) #같은 표현으로 c언어 대응서식 문자(%s), 숫자(%f)로 표현

if bmi < 20:
    print("저체중입니다")
elif bmi < 25:
    print("정상입니다")
elif bmi < 30:
    print("과체중입니다")
else:
    print("비만입니다")
