#student클래스를 외부에서 사용하기(모듈로 사용하기 파일은 student.py이고 해당 파일 위치와 다른 곳에서 현재 파일 생성)
#객체 리스트 사용하기
from classlib.student import Student #모듈에 소속되어 있는 클래스를 사용하겠다

'''
s = Student("김하나", 3)
print(s)
'''

s = [
    Student("김하나", 3),
    Student("이두울", 1),
    Student("박세엣", 2),
]

print("********* 학생 명단 *********")
for i in s: #전체 출력
    print(i)
