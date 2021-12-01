#파일 읽기

f = open("c:/web_dev/pyfile/season.txt", 'r') #읽기 모드 - 'r'사용
#season = f.readline() #첫 줄 읽기
#print(season)

seasons = f.readlines() #전체 라인 읽기, 리스트로 반환해서 저장
print(seasons)
#print(seasons[0]) #인덱싱 활용

#전체 읽기
for season in seasons:
    print(season.strip()) #공백 제거 포함

f.close() #파일 닫기