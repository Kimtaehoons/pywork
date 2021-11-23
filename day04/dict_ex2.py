#딕셔너리의 추가, 변경, 삭제, 조회
d = {'태훈' : 13, '하은' : 9}
print(d)
d['송희'] = 10 #요소 추가
print(d)
d['하은'] = 14
print(d)
#함수를 써서 키, 값 가져오기
d.keys()
print(d.keys())
print(d.values())
print(d.items())
#위 처럼 객체 출력이 아닌 값으로 전체 출력
for key, value in d.items():
    print(key, value)
#요소 삭제
print(d.pop('태훈'))
#출력
print(d)