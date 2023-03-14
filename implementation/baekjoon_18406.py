n = int(input())   # 점수
a = list(str(n))
half = len(a) // 2   # 가운데

front_sum = 0   # 반을 기준으로 왼쪽 부분의 각 자릿수의 합
back_sum = 0   # 오른쪽 부분의 각 자릿수의 합

for i in range(half):
    front_sum = front_sum + int(a[i])

a.reverse()

for i in range(half):
    back_sum  = back_sum + int(a[i])
    
if front_sum == back_sum :
    print("LUCKY")
else:
    print("READY")