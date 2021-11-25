#가변 매개변수(매개변수 앞에 *를 붙인다)
def calc_avg(*number):
    sum_v = 0 #합계 변수 선언
    for i in number:
        sum_v += i
    avg = sum_v / len(number)
    return avg

avg1 = calc_avg(1, 2) #calc_avg함수를 만들고 매개변수 1, 2를 넣었음
avg2 = calc_avg(1, 2, 3)
print(avg1)
print(avg2)