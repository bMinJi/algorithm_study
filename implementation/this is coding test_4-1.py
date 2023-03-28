# 상하좌우

n = int(input())   # 공간의 크기
moves = input().split()   # 이동 계획
x, y = 1, 1   # 시작 좌표

for move in moves:
    if move == 'L':   # 왼쪽으로 이동
        if y > 1:
            y = y - 1
    elif move == 'R':   # 오른쪽으로 이동
        if y < n:
            y = y + 1
    elif move == 'U':   # 위로 이동
        if x > 1:
            x = x -1
    elif move == 'D':   # 아래로 이동
        if x < n:
            x = x + 1

print(x, y)   # 도착지점 출력


        




