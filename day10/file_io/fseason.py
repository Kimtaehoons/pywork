#파일에 리스트 자료구조 저장하기
season = ['봄', '여름', '가을', '겨울']
f = open("c:/web_dev/pyfile/season.txt", 'w') #쓰기 모드 - 'w'
for i in season:
    f.write(i + '\n') #파일에 쓰기
f.close()

try: #파일 경로 오류나 파일 이름 오류로 인한 error방지
    f = open("c:/web_dev/pyfile/season.txt", 'r') 
    season = f.read()
    print(season)
except FileNotFoundError:
    print("파일을 열 수 없습니다")