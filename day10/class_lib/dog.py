#Dog클래스 만들기
class Dog:
    kind = "진돗개" #클래스 변수(공유됨)

    def __init__(self, name):
        self.name = name #인스턴스 멤버 변수

dog1 = Dog("백구")
dog2 = Dog("흰둥이")

print(dog1.kind) #shared 종(클래스 변수)
print(dog1.name) #unique 이름(인스턴스 변수)
print(dog2.name) #unique 이름(인스턴스 변수)
