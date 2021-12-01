#예외 처리 미루기
#사용하는 곳에서 예외를 처리함
class Animal:
    def cry(self):
        print("소리를 낸다")
        raise NotImplementedError #아래 동물마다 각기 구현하지 않으면 pass에 대한 에러 발생, 반드시 cry에 대해 다시 구현해라, 왜냐하면 동물마다 소리를 내는 소리가 다르기 때문

class Dog(Animal): #Animal 상속 받음(cry를 쓸 필요없다는 내용) class를 별도의 파일로 만들지 않아도 됨
    #pass
    def cry(self): #cry재정의
        print("왈~ 왈~")

class Cat(Animal):
    #pass
    def cry(self):
        print("야~옹 야~옹")

dog = Dog()
dog.cry()

dog = Cat()
dog.cry()