#예외 처리(Exception클래스)

try:
    x = int(input("숫자를 입력하세요 : "))
    print(x)

except ValueError:
    print("유효한 숫자가 아닙니다. 숫자를 입력해주세요")