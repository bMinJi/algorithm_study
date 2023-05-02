# 최대수 구하기 

# t = int(input())

# for test_case in range(1, t+1):
#     num = list(map(int, input().split()))
#     num.sort()
#     print("#{} {}" .format(test_case, num[9]))

t = int(input())

for test_case in range(1, t+1):
    num = list(map(int, input().split()))
    print("#{} {}".format(test_case, max(num)))