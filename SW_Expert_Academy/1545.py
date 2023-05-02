# 거꾸로 출력해 보아요

# t = int(input())
# result = []

# for i in range(0, t+1):
#     result.append(t)
#     t -= 1
# print(*result)   # 리스트 출력할때 [] 없이 요소만 출력

t = int(input())

for i in range(t, -1, -1):   # range(start, stop, step)
    print(i, end=" ")

