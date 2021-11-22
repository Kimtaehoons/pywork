#p.146
#1
a = "Life is too short, you need python"
if "wife" in a:
    print("wife")
elif "python" in a and "you" not in a:
    print("python")
elif "shirt" not in a:
    print("shirt")
elif "need" in a: #이 문장은 맞지만 이미 위의 문장이 맞아서 여기까지 내려오지 않고 위에서 끝나고 빠져나오기 때문에 출력이 되지 않느다
    print("need")
else:
    print("none")

#2
result = 0
count = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
        count += i
    i += 1
print("합계 : ", result)
print("개수 : ", count)

#3
i = 0
while True:
    i += 1
    if i > 5:
        break #i가 6일 때, while문이 True가 되므로 print되지 않고 빠져나온다
    print("*" * i) #True값이 아닐 때까지 print된다

#4
for i in range(1, 101):
    print(i)

#5
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
average = total / len(A)
print(average)