# 큰 놈, 작은 놈, 같은 놈

# t = int(input())

# for test_case in range(1, t+1):
#     num = list(map(int, input().split()))
#     left = num[0]
#     right = num[1]
#     if left == right:
#         result = "="
#     elif left > right:
#         result = ">"
#     else:
#         result = "<"
#     print("#{} {}".format(test_case, result))

# 조금 더 간단한 방법 
t = int(input())

for test_case in range(1, t+1):
    left, right = map(int, input().split())
    
    if left < right:
        result = "<"
    elif left > right:
        result = ">"
    else:
        result = "="
    
    print("#{} {}".format(test_case, result))