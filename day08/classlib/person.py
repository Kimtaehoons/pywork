'''
person클래스 만들기
접근 제한 방법 - 변수 이름 앞에 _(언더스코어)를 1개 또는 2개를 붙임
그래서 속성이 private로 바뀜
그러면 접근은 get + 변수이름(), set + 변수이름()으로 만들어 속성을 public으로 바꿈
'''

class Person:
    def __init__(self):
        self._name = "" #멤버 변수 초기화, 접근 제한
        self._age = 0

    def setname(self, name): #이름을 입력하는 함수
        self._name = name

    def getname(self): #이름을 가져오는 함수
        return self._name

    def setage(self, age): #이름을 입력하는 함수
        self._age = age

    def getage(self): #이름을 가져오는 함수
        return self._age

p1 = Person()
p1.setname("김하늘")
p1.setage(25)
print(p1.getname())
print(p1.getage())
