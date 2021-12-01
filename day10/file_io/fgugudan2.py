#구구단 파일 쓰기
#with ~ as문은 f.close()를 사용하지 않음
with open('gugudan.txt', 'w') as f: #상대 경로로 지정해 같은 위치에 파일 생성, 추가 쓰기 모드 - 'a'
    for i in range(2, 10): #전체 구구단 출력
        for j in range(1, 10):
            times = "%d x %d = %d\n" % (i, j, i*j)
            f.write(times)
        f.write('\n')