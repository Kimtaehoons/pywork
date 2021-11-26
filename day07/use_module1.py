#방법1. from 패키지.모듈이름 import 함수이름
from myModule.food import cook,eat
from myModule.calculator import add, sub

#food.py 사용
cook()
eat()

#calculator.py 사용
print(add(10, 2))
print(sub(10, 2))
