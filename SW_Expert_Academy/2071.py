# 평균값 더하기

t = int(input())

for test_case in range(1, t+1):
    num = list(map(int, input().split()))
    avg = 0
    cnt = 0
    for i in num:
        avg += i
        cnt += 1
    avg = avg / cnt
    print("#{} {:.0f}".format(test_case, avg))
               