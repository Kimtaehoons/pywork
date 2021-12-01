#파일 쓰기
f = open("c:/web_dev/pyfile/file.txt", 'w') #객체 생성(파일 열기), w를 쓰고 run을 하면(지금 창에서는 확인이 되지 않지만) 파일 저장위치에 txt파일 생성됨
f.write("하늘이 파랗다\n")
f.write("Thank you!!\n")
f.write("大韓民國\n")
#f.write(45) #숫자를 바로 저장할 수 없음
#f.write("45\n") #문자형태로 입력하여 숫자처럼 입력이 가능하나
f.write("%d\n" % (45+12)) #계산이 가능하도록 숫자형으로 입력

f.close() #파일 닫기