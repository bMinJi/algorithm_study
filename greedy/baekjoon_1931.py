# 회의실 배정

n = int(input())   # 회의의 수
time = []

for i in range(n):
    start, end = map(int, input().split())
    time.append([start, end])

time = sorted(time, key = lambda x : x[0])   # start 기준으로 정렬
time = sorted(time, key = lambda x : x[1])   # end 기준으로 정렬

last_end = 0
cnt = 0   # 회의 갯수

for start, end in time:
    if start >= last_end:
        cnt += 1
        last_end = end
        
print(cnt)