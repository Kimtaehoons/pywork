#while반복문
#1~10까지 전체값, 합계값 출력
i = 0
sum_v = 0
while i < 10:
    i += 1#i = i + 1
    sum_v += i

print("i=", i)#현재 i는 10이다. 11이면 빠져나오기 때
print("sum=", sum_v)

#1~10까지 짝수값 출력
i = 0#i가 10인 것을 다시 초기화시킴
while i < 10:
    i += 1
    if i % 2 == 0:
        print(i, end=' ')#끝이 공백이다라고 해주면 옆으로 찍힌다
        
