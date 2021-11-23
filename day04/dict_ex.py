#딕셔너리(dictionary)
#키(key)와 값(value)의 쌍
person = {} #빈 딕셔너리 생성
person["name"] = "한국민"
person["age"] = 27
person["phone"] = "010-0000-0000"
print(person)
#수정
person["age"] = 30
print(person)
print(type(person))
#삭제
del person["phone"]
print(person)
#위 처럼 객체 출력이 아닌 값으로 전체 출력
for key in person:
    #print(key) #key 출력
    print()
    #print(person[key]) #value 출력
    print()
    print(key, ':', person[key]) #한 줄로 출력