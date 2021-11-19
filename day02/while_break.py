#while~break문
#1~10까지 전체 출력
"""
i = 0
while True:
    i += 1
    if i > 10:
        break(#i가 11일 때 break)
    print(i)(#i가 10까지는 False이므로 출력)
"""

#키가 'y'이면 "계속 반복", 'n'이면 "반복 중단", 그 이외의 키는 "정상 답변이 아님"
while True:
    key = input("반복을 계속할까요?(y/n)")#키로 입력받음
    if key == 'y' or key == 'Y':
        print("계속 반복")
    elif key == 'n' or key == "N" :
        print("반복 중단")
        break
    else:
        print("정상 답변이 아님")
