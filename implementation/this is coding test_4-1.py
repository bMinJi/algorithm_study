# 상하좌우

n = int(input())
moves = input().split()
x, y = 1, 1

for move in moves :
    if move == 'L' :
        if y > 1 :
            y = y - 1
    elif move == 'R' :
        if y < n :
            y = y + 1
    elif move == 'U' :
        if x > 1 :
            x = x - 1
    elif move == 'D' :
        if x < n :
            x = x + 1        

print(x, y) 
        

