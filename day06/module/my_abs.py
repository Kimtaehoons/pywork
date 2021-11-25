#절대값 함수 구현하기
#절대값 알고리즘
import math

def myabs(x):
    if x < 0:
        return -x
    else:
        return x

#절대값 알고리즘2
def myabs2(x):
    y = x * x #제곱을 하고 나서 1.
    return int(math.sqrt(y)) #2. 제곱근 실시

print(myabs(-3)) #사용자 정의 함수
print(myabs2(-3)) #사용자 정의 함수
print(abs(-3))
