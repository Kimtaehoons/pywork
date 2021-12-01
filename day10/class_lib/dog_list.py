#Dog클래스 만들기(day08의 cart.py와의 비교)
class Dog:
    #tricks = [] #클래스 리스트 여기에 선언하면 각각 기술 적용이 안 되므로 아래에 넣어준다

    def __init__(self, name):
        self.name =  name
        self.tricks = [] #인스턴스 멤버 리스트

    def add_trick(self, trick): #외부 함수 호출해서 trick이 들어감
        self.tricks.append(trick)

dog1 = Dog("Elsa")
dog2 = Dog("Buddy")
dog1.add_trick("play dead")
dog2.add_trick("roll over")
print(dog1.tricks)
print(dog2.tricks)