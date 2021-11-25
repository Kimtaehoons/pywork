#1~100까지의 수 중에서 배수 출력

def times(x):
    global count
    for i in range(1, 101):
        if i % x == 0: #x가 무슨 값인지 모르기때문에 3이 아니다
            count += 1
            print(i, end=' ')

count = 0
times(3) #return을 받을 때는 print를 해야하지만 print를 했을 떄는 중복돼 none이 나오므로 삭제
print("\n3의 배수의 개수 : " + str(count) + "개") #전역변수로 개수 세기

def times(x):
    count = 0
    for i in range(1, 101):
        if i % x == 0: #x가 무슨 값인지 모르기때문에 3이 아니다
            count += 1
            print(i, end=' ')
            print("\n3의 배수의 개수 : " + str(count) + "개") #지역변수로 개수 세기

times(3) #return을 받을 때는 print를 해야하지만 print를 했을 떄는 중복돼 none이 나오므로 삭제