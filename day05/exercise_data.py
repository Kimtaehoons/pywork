#연습문제
1.
A = [80, 75, 55]
total = 0
for score in A:
    total += score
average = total / len(A)
print(average)

"""(객체 정의해서 하는 방법 미작성)
국어, 영어, 수학 = (80, 75, 55)
sum_v = 
avg = sum_v / count
print(avg)
"""

2.
a = 13
if a % 2 == 0:
    print(a, "는 짝수")
else:
    print(a, "은 홀수")

3.
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)

4.
pin = "881120-1068234"
print(pin[7])

5.
a = "a:b:c:d"
x = a[1::2]
print(x)