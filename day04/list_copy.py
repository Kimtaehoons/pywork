a1 = [1, 2, 3, 4]
a2 = [] #빈 리스트 생성
a3 = []
#a1에 5를 저장
a1.append(5)
print(a1)
#복사 저장(a1->a2)
for i in a1:
    a2.append(i) #i++개념이 담겨있다
print(a2)
#복사 저장(a1(홀수만)->a3)
for i in a1:
    if i % 2 == 1:
        a3.append(i)
print(a3)