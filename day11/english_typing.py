#영어 타자 게임
import random as r
import time

#단어를 랜덤하게 추출하기
with open("word.txt", 'r') as f:
    word = f.readline().split() #한 줄로 공백 제거되고 단어 전체가 공백문자로 구분돼 출력

n = 1 #문제 번호
input("[타자게임] 준비되면 엔터! ")
start = time.time()
while n < 11:
        print('-문제', n)
        question = r.choice(word) #문제 단어 출제
        print(question)
        answer = input()               #정답 입력
        #통과(+n 증가) 아니면 오타 코드 작성
        if answer == question:
                print("통과!")
                n += 1 #맞은 문제만 n이 증가
        else:
                print("오타! 다시 도전!")
end = time.time()
print("게임 소요 시간 : %.2f초" % (end-start))