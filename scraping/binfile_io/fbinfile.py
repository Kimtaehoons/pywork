#바이너리 파일 쓰기(wb)
with open('data.bin', 'wb') as f:
    text = "비가 내린다"
    f.write(text.encode()) #text를 encoding함
    
#바이너리 파일 읽기(rb)
with open('data.bin', 'rb') as f:
    data = f.read()
    text = data.decode() #코드화된 text를 decoing함
    print(text)

