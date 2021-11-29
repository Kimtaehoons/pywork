#Counter 클래스
#인스턴스 변수(클래스 변수와 대응하는 개념) - 담을 때마다 새롭게 담는 개념
class Counter:
    def __init__(self):
        self.x = 0 #시작 0으로 초기화(인스턴스 변수)
        self.x += 1

    def getcount(self):
        return self.x

c1 = Counter() #c1은 인스턴스 객체
print(c1.getcount()) #1

c2 = Counter() #부를 때마다 init에서 시작 0으로 초기화되기 때문
print(c2.getcount()) #1