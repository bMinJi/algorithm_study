# 연원일 달력

t = int(input())

# month를 key, day를 value
days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

for test_case in range(1, t+1):
    # 해당 날짜를 문자열로 받은 후, year, month, day로 문자열 인덱싱
    date = input()
    year = date[:4]
    month = date[4:6]
    day = date[6:]

    # month는 1~12, day는 0보다 크고 해당 일보다 작거나 같을때
    if 0 < int(month) < 13 and 0 < int(day) <= days[int(month)]:
        result = year + '/' + month + '/' + day
    else:
        # 조건을 만족하지 못할때
        result = '-1'

    print("#%d %s" %(test_case, result))