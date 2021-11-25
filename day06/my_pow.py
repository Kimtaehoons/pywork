#거듭제곱 함수 만들기
def my_pow(x, y): #x가 밑, y가 지수
    num = 1 #곱셈 초기화는 1
    for i in range(y):
        num *= x
    return num
print(my_pow(2, 4)) #사용자 정의 함수 호출
print(pow(2, 4)) #내장 함수 호출