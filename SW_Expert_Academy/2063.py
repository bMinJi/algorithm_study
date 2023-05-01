# 중간값 찾기

t = int(input())
num = list(map(int, input().split()))
num.sort()
middle = num[t//2]
print(middle)




    