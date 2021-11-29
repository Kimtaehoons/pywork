#방법2. from 패키지 import 모듈이름
from myModule import food
from myModule import calculator

#food.py 사용
food.cook()
food.eat()
food.sleep()

#calculator.py 사용
print(calculator.add(10, 2))
print(calculator.sub(10, 2))