#1부터 n까지 곱하기
#기존 방식(반복문)
def facto(n):
    gob = 1
    for i in range(1, n+1):
        gob *= i
    return gob

print(facto(1)) #1*1
print(facto(2)) #1*2
print(facto(3)) #1*3
print()

#위의 내용을 재귀함수로 작성(조건문)
def facto(n):
    if n <= 1: #최종 값(마지막 값)
        return 1
    else:
        return n * facto(n-1) #마지막보다 큰 값

print(facto(1)) #1 #if로 들어감
print(facto(2)) #2*facto(1) #else로 들어감
print(facto(3)) #3*facto(2)