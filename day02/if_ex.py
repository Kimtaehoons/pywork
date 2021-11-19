#if문
age = 6
if age < 8:
        print("학교에 갈 나이가 아닙니다")#들여쓰기 - 인덴트(4칸)으로 코드블럭대체
print("나이는 " + str(age) + "세 입니다")
      
#if~else문
speed = int(input("속도 입력: "))
#print()괄호 안 내용이 input안으로, 숫자는 int로 감싸준
if speed > 50:
    print("속도 위반, 과태로 10만원")
else:
    print("안전 속도 준수!!")
