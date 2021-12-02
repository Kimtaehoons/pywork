#2차원 리스트 만들기
with open('animal.txt', 'w') as f:
    animal = ['dog', 'cat', 'cow', 'pig']

    #파일에 쓰기
    for i in animal:
        f.write(i + '\n')

#animal.txt읽기
with open('animal.txt', 'r') as f:
    #animal = f.readlines() #1차원 리스트
    #print(animal)
    animal = []
    for i in range(4):
        animal.append(f.readline().split())
    print(animal) #2차원 리스트(2차원에 넣어야지 계산을 할 수 있음, 콘솔 창에서는 가로로 나열된 것처럼 보이나, 1행 0열, 2행 0열, 3행 0열, 4행 0열로 돼 있음)