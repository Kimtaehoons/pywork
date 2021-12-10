import re

str = "Two is too"
m1 = re.findall("T[ow]o", str)
print(m1)

m2 = re.findall("T[ow]o", str, re.IGNORECASE) #IGNORECASE대소문자 구별하지 않음
print(m2)

m3 = re.findall("t[^w]o", str) # ^은 부정(not)
print(m3)