import re

#compile함수의 매개변수로 정규식 사용(byte코드로 바꿈)
p = re.compile("[a-z]") #a~z까지 소문자
p.match("afternoon")
m = p.match("afternoon") #match함수는 첫 문자부터 일치 여부를 결과로 반환(즉, 첫 문자가 일치하면 결과를 반환하고, 일치하지 않으면 None을 반환)
print(m)

p = re.compile("[a-z]+") #a~z까지 반복되는 소문자
p.match("afternoon")
m = p.match("afternoon")
print(m)

m2 = p.match("2021 python")
print(m2)

s = p.search("2021 python") #search함수는 전체를 검색해서 일치하면 결과를 반환
print(s)

