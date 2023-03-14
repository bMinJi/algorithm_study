# 동전 O

n, k = map(int, input().split())   # n = 동전의 종류, k = 합
coin_list = []

for i in range(n):
    coin = int(input())   # n개의 돈
    coin_list.append(coin)
    
coin_list.reverse()   # 큰 단위부터 계산하기 위해서
count = 0   # 동전 개수

for i in coin_list:
    count = count + k // i   # 카운트 값에 K를 동전으로 나눈 몫을 더한다
    k = k % i   # K는 동전으로 나눈 나머지 

print(count)



