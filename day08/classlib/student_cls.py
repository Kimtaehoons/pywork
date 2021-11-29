#student 클래스 만들기
#class는 self키워드를 사용
#def init, 생성자(constructor) 함수 사용
class Student:
    def __init__(self): #initial(생성자)
        self.name = "콩쥐" #멤버 변수
        self.grade = 1
        print("생성자 함수입니다") #제일 먼저 출력되는 것을 확인

    def learn(self):
        return ("수업을 듣습니다")

s = Student()
#매개변수가 없는 생성자(constructor) 함수
#Student클래스의 객체(object, 인스턴스)인 s 생성
#주기억장치에서 작동이 된다는 것을 print를 통해서 알 수 있는 것(print를 한다고 뭘 하는 것은 아니기때문)
print("이름 : " + s.name)#s를 찍었을 때 앞에 f가 멤버
print("학년 : " + str(s.grade))
print(s.learn()) #모듈함수에서 return을 했기 때문에 여기서 print를 해줘야한다. 모듈함수에서 바로 print를 했을 때는 여기서 print가 필요없음