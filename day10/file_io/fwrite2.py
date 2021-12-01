#파일 쓰기
f = open("c:/web_dev/pyfile/number.txt", 'w') #객체 생성(파일 열기), w를 쓰고 run을 하면(지금 창에서는 확인이 되지 않지만) 파일 저장위치에 txt파일 생성됨
f.write("%d\n" % 45)
f.write("%.2f\n" % 12.34)
f.write("%d\n" % (45+12)) #괄호 생략하면 안 됨
i = 3
j = 4
times = "%d x %d = %d" % (i, j, i*j)
f.write(times)

f.close() #파일 닫기