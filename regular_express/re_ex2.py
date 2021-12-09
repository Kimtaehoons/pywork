import re

#방법1.
str = "123?45yy7890"
pat = re.compile("[0-9]{1,3}") #숫자를 1~3 검색
m = re.findall(pat, str)
print(m)

#방법2.(방법1과 동일한 코딩)
str = "123?45yy7890"
m = re.findall("[0-9]{1,3}", str)
print(m)


