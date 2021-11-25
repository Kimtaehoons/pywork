#기본 매개변수
#함수를 통한 문자 출력
def print_string(text, count = 1): #count 기본매개 변수를 초기화여 선언
    for i in range(count):
        print(text)

print_string("Hello~") #count 생략 호출(함수 호출 시 생략하면 기본값으로 출력)
print_string("Hello~", 3) #count에 3을 줘 위에서 3번 반복 하게끔 한다
