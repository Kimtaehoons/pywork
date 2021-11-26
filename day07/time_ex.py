import math
import time

print(time.time()) #1970. 1. 1(유닉스 운영체제 설립) 자정이후부터 현재까지 초로 환산
days = round(time.time() / (24*60*60)) #초를 일자로 환산
years = round(time.time() / (365*24*60*60)) #초를 년도로 환산

print("{}".format(days))
print("{}".format(years))

#time.sleep(x) #x초만큼 시간 간격을 둠
#for문 수행 시간 측정
start = time.time()
for i in range(20):
    print(i)
    time.sleep(0.5) #파이썬 1 - 1초, 다른언어 1000 - 1초
end = time.time()
et = math.floor(end-start)
print("for문 수행 시간 : {}초".format(et))