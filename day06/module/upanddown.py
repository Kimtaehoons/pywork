import random

com = random.randint(1, 100)
min_v = 1
max_v = 100
for i in range(10):
    try: #입력값(자료) 예외처리
        guess = int(input("맞혀보세요([%d회] %d~%d) -> " % (i+1, min_v, max_v))) #사용자가 추측한 숫자
        if guess > 100 or guess < 1: #입력값(범위) 오류처리
            print("입력 범위를 초과했어요. 다시 입력해주세요")
        elif guess == com:
            print("정답!!")
            break
        elif guess > com:
            print("너무 커요!")
            max_v = guess
        else:
            print("너무 작아요!")
            min_v = guess
    except:
        print("숫자가 아닙니다. 다시 입력해 주세요")
print("정답 : %d" % com)
print("점수 : %d" % ((10 - i) * 10))