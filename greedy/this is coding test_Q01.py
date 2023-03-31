# 모험가 길드

n = int(input())   # 모험가 수 
fear = list(map(int, input().split()))   # 각 모험가의 공포도 값
groupNum = 0   # 그룹에 포함된 모험가 수
result = 0   # 총 그룹 수 

fear.sort()   # 오름차순 정렬

for x in fear:
    groupNum = groupNum + 1   # 그룹에 모험가 포함시키기
    if groupNum >= x:
        result = result + 1   # 총 그룹의 수 증가
        groupNum = 0   # 그룹에 포함된 모험가 수 초기화

print(result)
