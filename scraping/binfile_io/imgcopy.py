#이미지 파일 복사하기(읽어서 쓰기)
#다른 폴더에 있는 이미지 해당 폴더로 복사하기
with open("../healing.jpg", 'rb') as f1: #상위폴더에 있는 가져올 이미지 경로
    pic = f1.read()

with open("./healing2.jpg", 'wb') as f2: #만들 파일이름 임의로 설정
    f2.write(pic)








