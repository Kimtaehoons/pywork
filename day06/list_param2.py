#리스트를 매개변수로 새로운 리스트 만들기
def times(a): #v가 a로 가짜 복사된 것
    li = [] #새로운 빈 리스트
    for i in a:
        li.append(i)
    return li #times(v)대신 바뀐 리스트의 값으로 출력된다
    
v = [5, 9, 3, 8]
print(times(v))