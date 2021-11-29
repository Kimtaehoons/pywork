#거북이 대포 게임
#각도를 맞춰 대포를 발사해 목표지점을 맞히는 게임
import turtle as t
import random as r

'''좌표 이동 연습
#좌표 이동 함수 - t.goto(x, y)
t.up()
t.goto(0, 200) #x좌표 : 0, y좌표 : 200
t.goto(200, 0) #x좌표 : 200, y좌표 : 0
'''
#화살표 각도 조절 함수 이용(함수는 위에서 설정0
def turn_up():
    t.left(2)
def turn_down():
    t.right(2)
def fire():
    ang = t.heading() #게임을 하고 움직인 각도 저장
    
    while t.ycor() > 0: #화살표의 y좌표가 0보다 크면(땅 위에 있는 동안)
        t.forward(15) #15픽셀만큼 직진하면서
        t.right(5) #오른쪽으로 5도만큼 돌림
    #while반복문을 빠져 나오면 땅에 닿은 상태임
    d = t.distance(target, 0) #화살표와 목표지점과의 거리 저장
    t.sety(r.randint(10, 100)) #성공 또는 실패를 표시할 위치 지정

    if d < 25: #명중 처리
        t.color('blue')
        t.write("good!", False, "center", ("", 15)) #글자쓰기 함수("문자열", 위치 이동하지 않음, "가운데 정렬", 글꼴 크기)

    else: #명중 처리 실패 시
        t.color('red')
        t.write("bad!", False, "center", ("", 15))
        t.color('black')
        t.goto(-200, 10) #화살표 처음 위치로 이동
        t.setheading(ang) #화살표 처음 각도로 이동

#땅 그리기
t.goto(-300, 0)
t.goto(300, 0)

#목표 지점 그리기
target = r.randint(50, 150) #목표지점 = 50~150사이의 임의의 수
t.color('green')
t.pensize(2)
t.up() #선 올리기

#이동
t.goto(target -25, 2)
t.down() #선 내리기
t.goto(target +25, 2)

#화살표 처음 위치 설정
t.color('black') #좌표 검은색으로 변경
t.up()
t.goto(-200, 10)

#화살표 각도 동작하는 설정
t.onkeypress(turn_up, "Up") #turn_up함수
t.onkeypress(turn_down, "Down")
t.onkeypress(fire, "space") #발사함수

t. listen()
t.mainloop()