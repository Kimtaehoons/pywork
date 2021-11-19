#자리배치도 프로그램
#고객 수를 열(좌석)로 나눠 행(줄)을 구해서 for문으로 배치
customer = int(input("입장객 수 입력 : "))
col = int(input("좌석 열 수 입력 : "))

"""          
row = customer // col
for i in range(0, row):
    for j in range(1, col+1):
        print(i*col+j, end=' ')
    print()
print()
"""
          
if customer % col == 0:
    row = customer // col#int(customer / col)
else:
    row = customer // col + 1
for i in range(0, row):
    for j in range(1, col+1):
        seat = i*col+j
        if seat > customer:
            break
        print("좌석" + str(seat), end=' ')
    print()
