# ATM

n = int(input())   # 사람의 수
time = list(map(int, input().split()))   # 사람이 돈을 인출하는데 걸리는 시간
time_sum = 0   # 각 사람이 돈을 인출하는데 필요한 시간
min_sum = 0  # 각 사람이 돈을 인출하는데 필요한 시간 합의 최솟값

time.sort()   # 정렬

for i in time:
    time_sum = time_sum + i
    min_sum = min_sum + time_sum   

print(min_sum)   