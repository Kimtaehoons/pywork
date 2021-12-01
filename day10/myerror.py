#예외만들기
#Exception클래스를 상속받아야 함
class MyError(Exception):
    def __str__(self): #객체(MyError())가 생성되면서 정보가 나오게끔 처리
        return "허용되지 않는 별명입니다"

def say_nick(nick): #class에서 빠져나왔으므로 self를 쓰지 않음
    if nick == "바보" or nick == "칠푼이": #or로 추가로 금칙어 설정 가능
        raise MyError()
    print(nick)

try:
    say_nick("영웅")
    #say_nick("바보")
    say_nick("칠푼이")
except MyError as e: #e는 MyError의 별칭
    print(e)