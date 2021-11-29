#계산기 클래스 정의
#기능 : 더하기, 빼기
class Calculator: #class객체를 사용해서 생성
    def __init__(self):
        self.x = 0

    def __add__(self, y):
        self.x += y
        return self.x

    def __sub__(self, y):
        self.x -= y
        return self.x

c = Calculator() #테스트
print(c.add(10))
print(c.sub(5))
