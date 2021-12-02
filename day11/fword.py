#english_typing(day07)에 리스트 내용 추가에 따른 txt파일 만들기
import random as r

with open("word.txt", 'w') as f:
    word = ['sky', 'earth', 'moon', 'flower', 'tree',
            'strawberry', 'grape', 'garlic', 'onion', 'potato']
    for w in word:
        f.write(w + ' ')

#단어를 랜덤하게 추출하기
with open("word.txt", 'r') as f:
    #word = f.readlines() #자료구조가 리스트구조로 반환
    word = f.readline().split(' ') #한 줄로 공백 제거되고 단어 전체가 공백문자로 구분돼 출력
    w = r.choice(word) #랜덤하게 단어 1개 추출
    print(w)