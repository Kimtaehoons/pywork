#Counter 클래스
#클래스 변수(인스턴스 변수와 대응하는 개념) - 장바구니에 담을 때 누적되는 개념
class Counter:
    x = 0

    def __init__(self): #클래스 변수 이름은 클래스 이름(Counter)으로 접근
        Counter.x += 1

    def getcount(self): #클래스 변수 이름은 클래스 이름(Counter)으로 접근
        return Counter.x

c1 = Counter()
print(c1.getcount()) #1

c2 = Counter()
print(c2.getcount()) #2