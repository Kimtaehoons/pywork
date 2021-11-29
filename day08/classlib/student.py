#매개변수가 있는 생성자(constructor) 함수(매개변수에 다른 변수도 받기 위함)
class Student:
    def __init__(self, name, grade): #생성자로 매개변수를 전달
        self.name = name
        self.grade = grade

    def __str__(self): #객체의 멤버정보를 출력하는 함수
        return "이름 : {}, 학년 : {}".format(self.name, self.grade)

if __name__ == "__main__": #name변수의 이름이 main일 때만(왜냐하면 다른 파일에서 이 모듈을 가져올 때 테스트 값이 따라나오기 때문에 여기서만 나오게끔 하는 조치)
    s1 = Student("콩쥐", 1) #s1 객체 생성
    s2 = Student("팥쥐", 2) #s2 객체 생성
    print(s1)
    print(s2)