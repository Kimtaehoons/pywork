#방법1. from 패키지.모듈이름 import 함수이름
from myModule.food import cook, eat, sleep
from myModule.calculator import add, sub

#food.py 사용
cook()
eat()
sleep()

#calculator.py 사용
print(add(10, 2))
print(sub(10, 2))
