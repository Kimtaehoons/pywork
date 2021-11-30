#Person클래스
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self): #객체(p)
        return "이름 : {}, 나이 : {}".format(self.name, self.age)

if __name__ == "__main__": #자식 모듈에 나오지 않게함
    p = Person("김하늘", 21) #객체(오브젝트, 인스턴스)p 생성
    print(p)