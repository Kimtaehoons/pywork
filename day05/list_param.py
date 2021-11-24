#리스트를 매개변수로 전달하기
#점수의 평균 계산하기
def calc_avg(a):
    sum_v = 0
    count = 0
    for i in a:
        sum_v += i
        count += 1
    avg = sum_v / count
    return avg #호출한 쪽(calc_avg(v)으로 보내준다(작성 순서 : 2)

v = [70, 90, 50, 80, 100] #리스트를 매개변수로 넘긴다(작성 순서 : 1)
average = calc_avg(v)

print("평균 : %.1f점" % average)