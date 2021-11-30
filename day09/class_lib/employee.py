#Employee클래스 정의
from day09.class_lib.person import Person #Person클래스 상속 경로

class Employee(Person): #Person클래스를 상속받음
    #pass
    def __init__(self, name, age, employeeID):
        super().__init__(name, age) #상속 받은 부모 멤버를 super()함수로 명시해 효율성도 추구
        self.employeeID = employeeID #자기 멤버 초기화
    def __str__(self): #부모 __str__()함수 상속 : 재정의(method overriding) 즉, 부모 함수와 동일한 형태에 자기 멤버를 받는 것을 추가함
        return super().__str__() + ", 사번 : " + str(self.employeeID) #앞에 건 부모 멤버 함수를 받는 함수와 + 뒤에 건 자기 멤버를 받는 함수 정의

e = Employee("이강", 25, 101)
print("이름 : " + e.name) #상속 받았기 때문에 부모 멤버(name, age)에 접근 가능
print("나이 : " + str(e.age)) #상속 받았기 때문에 부모 멤버(name, age)에 접근 가능
print("사번 : " + str(e.employeeID)) #자식 클래스에 새로 생성된 멤버(employeeID)에 따라 부모 멤버와 구분을 줘야 오류가 안 남
print(e) #사번이 보이지 않음 그래서 return super()로 부모 멤버 함수와 자기 멤버를 받는 함수를 위에서 정의해야함