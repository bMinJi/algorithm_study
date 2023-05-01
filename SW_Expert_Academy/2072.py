# 홀수만 더하기

n = int(input())   # 테스트 케이스 개수

for i in range(1, n+1):
    # 테스트 케이스 개수만큼 입력받아 리스트에 넣기
    num = list(map(int, input().split()))
    sum = 0
    # 홀수라면 더한 후 출력
    for j in num:
        if j % 2 == 1:
            sum += j
    print("#%d %d" %(i, sum))

        


