import turtle

turtle.shape('turtle')

'''
turtle.forward(100) #100픽셀만큼 앞으로 이동
turtle.left(90) #머리 방향을 왼쪽으로 90도 회전
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
'''

#위의 것을 for반복문으로 구현(반복문 응용)
for i in range(4):
#움직이면서 사각형 만들기
    turtle.forward(100)
    turtle.left(90)
#움직이면서 삼각형 만들기
for i in range(3):
    turtle.forward(100)
    turtle.left(120) #각도 120도
#움직이면서 원 만들기
turtle.circle(50)

turtle.mainloop()