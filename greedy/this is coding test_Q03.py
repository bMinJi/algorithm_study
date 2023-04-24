# 문자열 뒤집기 (백준 1439)

s = input()

# 0으로 바뀔때 count, 1로 바뀔때 count
cnt0 = cnt1 = 0

# 첫 번째 원소
if s[0] == '0':
    cnt1 += 1
else:
    cnt0 += 1

# 입력받은 문자열 길이만큼
for i in range(len(s) - 1):
    if s[i] != s[i+1]:
        if s[i+1] == '0':
            cnt1 += 1
        else:
            cnt0 += 1

print(min(cnt0, cnt1))

