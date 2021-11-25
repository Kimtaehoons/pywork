#전역변수
def one_up(): #2. 함수를 정의
    global x
    x += 1
    return x
x = 1 #main에 적은 전역변수 x라 프로그램이 종료될 때 메모리에서 해제 - 누적된 값이 필요할 때 사용

print(one_up()) #1. 호출할 함수를 만든다
print(one_up())