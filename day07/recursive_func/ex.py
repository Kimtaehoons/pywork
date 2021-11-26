#재귀함수 - 자신을 호출하는 함수
#기존 방식인 반복문으로 작성
def sos1(n):
    for i in range(n):
        print("Help me!!")
sos1(5)
print()

#위의 내용을 다른 알고리즘인 재귀함수로 작성
def sos2(n):
    if n < 1:
        return ""
    else:
        print("Help me!!")
        return sos2(n-1)
sos2(5)
#수기 디버깅
#sos2(5) #Help me!!
#sos2(4) #Help me!!
#sos2(3) #Help me!!
#sos2(2) #Help me!!
#sos2(1) #Help me!!
#sos2(0) #공백