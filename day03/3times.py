#3의 배수(1~20)
count = 0#전역변수
sum = 0
for i in range(1, 21):
    if i % 3 == 0:#지역변수
        print(i, end='')
        count += 1
        sum += i
avg = sum / count
#i = 3, count = 0 + 1
#i = 6, count = 1 + 1 ...
print()
print("3의 배수의 개수 : ", count)
print("3의 배수의 합계 : ", sum)
print("3의 배수의 평균 : ", avg)
