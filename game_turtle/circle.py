#여러 개의 원 그리기
import turtle as t #turtle을 t라고 부른다

n = 100
t.speed(0) #속도 : 1~10, 가장 빠른 속도 : 0
t.bgcolor('pink') #무대 배경 색
t.color('green') #도형(원) 색
for i in range(n):
    t.circle(100)
    t.left(360/n)

t.mainloop()