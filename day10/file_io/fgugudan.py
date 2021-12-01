#구구단 파일 쓰기
#with ~ as문은 f.close()를 사용하지 않음
with open('99.txt', 'a') as f: #상대 경로로 지정해 같은 위치에 파일 생성, 추가 쓰기 모드 - 'a'
    dan = 7
    for i in range(1, 10):
        times = "%d x %d = %d\n" % (dan, i, dan*i)
        f.write(times)
    f.write('\n')