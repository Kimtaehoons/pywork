#리스트의 생성 및 관리
#정수형 리스트 생성 및 초기화
number = [10, 20, 30, 40]
#요소 개수(길이)
print(len(number))
print()

#for ~ in문 #배열값 출력
for i in number:
    print(i)
print()

#for ~ range()문
n = len(number)
for i in range(0, n): #range는 어차피 index로 받아서 0으로 시작하니 끝값은 하나 뺀 값과 같은 이치
    print(number[i], end = '')

#요소 추가
number.append(50) #맨 뒤로 추가
print(number)
print(type(number))

#요소 수정
number[1] = 60
print(number)

#요소 삭제
#del number[2] #del명령어로 삭제
number.pop(2) #함수로 삭제
print(number)
print()



