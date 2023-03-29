# 문자열 재정렬

s = input()   # 문자열 입력
result = []   # 결과 리스트
sum = 0   # 숫자합

for x in s:
    if x.isalpha():   # 문자를 하나씩 확인해서 알파벳인 경우 list에 담기
        result.append(x)
    else:
        sum = sum + int(x)   # 정수로 바꿔서 더하기

result.sort()   # 알파벳 오름차순 정렬
result.append(str(sum))   # 해당 정수를 문자열로 바꾼후 list에 담기

print(''.join(result))   # 리스트를 문자열로 변환하여 출력


    



