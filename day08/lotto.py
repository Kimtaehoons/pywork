#로또 복권 생성 프로그램
#1~45 중 6개 추첨(단, 중복되면 안 됨)
import random

lotto = [] #빈 리스트 준비

'''
#로또 복권 번호 1개 추첨
for i in range(0, 6): #0~5
    num = random.randint(1, 45)
    #문제발생1)조건문을 사용해서 번호 중복 문제 해결 필요
    #num이 기존 lotto 리스트에 없는 번호면
    if num not in lotto:
        lotto.append(num)  # 리스트에 num추가
    #문제발생2)중복이 발생했을 때 num이 출력이 되지 않아 개수가 모자라는 문제 해결 필요
    #while문으로 아래와 같이 재 코딩하고자 함
'''

while len(lotto) < 6: #0~5 -> 6개
    num = random.randint(1, 45)
    if num not in lotto:
        lotto.append(num)

print(lotto)