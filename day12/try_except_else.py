#try ~ except ~ else문
#에러가 없으면 try ~ else문 실행(except문 건너뜀), 에러가 있으면 try ~ except문 실행(else문 실행안 됨)
try:
    print("1번")
    with open('2021kbo.txt', 'r') as f:
        team = f.readlines()
except:
    print("2번")
    print("파일을 열 수 없습니다")
else:
    for i in team:
        print(i, end='')