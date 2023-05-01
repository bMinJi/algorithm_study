# 자릿수 더하기

n = int(input())

num = []
sum = 0
for i in str(n):
    num.append(i)
    sum += int(i)
print(sum)