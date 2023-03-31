# 곱하기 혹은 더하기

s = input()
result = int(s[0])   # 첫번째 문자를 숫자로 

for x in range(1, len(s)):
    # 첫번째 숫자가 1보다 작거나 혹은 다음 숫자가 1보다 작을 경우는 더하기
    num = int(s[x])
    if num <= 1 or result <= 1:
        result = result + num
    else:
        result = result * num

print(result)
