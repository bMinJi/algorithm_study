# 설탕 배달

n = int(input())  
bag = 0   # 봉지의 갯수

while n >= 0 :
    if n % 5 == 0:   # 5의 배수이면 
        bag = bag + n // 5   # 5로 나눈 몫을 봉지 갯수에 추가 
        print(bag)
        break
    n -= 3   
    bag += 1   # 3kg 봉지
else:
    print(-1)   # 나누어 떨어지지 않을때 -1 출력
    