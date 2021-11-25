#날짜, 시간 표시하는 모듈
import datetime

print(datetime.datetime.today())
print(datetime.date.today())

now = datetime.datetime.today()
print("{}년 {}월 {}일".format(now.year, now.month, now.day))
print("{}시 {}분 {}초".format(now.hour, now.minute, now.second))
print(now.strftime("%Y. %m. %d %H:%M:%S"))
