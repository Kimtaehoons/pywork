#파일 읽기
f = open("c:/web_dev/pyfile/file.txt", 'r') #읽기 모드 - 'r'사용
#f = open("c:/web_dev/pyfile/number.txt", 'r')
text = f.read() #파일 내용 전체 읽어서(보조기억장치) text로 담아서
print(text) #콘솔(메모리)에 출력
f.close() #파일 닫기