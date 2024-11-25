import calendar
from datetime import datetime

# 현재 날짜와 시간 가져오기
now = datetime.now()

# 현재 년도와 월 가져오기
year = now.year
month = now.month
month = now.month

# 이번 달의 첫 날의 요일과 날짜 수 계산
first_day_of_month = datetime(year, month, 1)
first_weekday = first_day_of_month.weekday()
num_days_in_month = calendar.monthrange(year, month)[1]

# 요일 이름 설정 (0: 월요일, 1: 화요일, ..., 6: 일요일)
weekdays = ['월', '화', '수', '목', '금', '토', '일']


month_days = [{'day': 0, 'week': '일'}]



# 시작 요일 이전의 공백 출력
for i in range(first_weekday):
    print('   ', end='')
    month_days.append({'day': 0, 'week': weekdays[i]})

# 날짜와 요일 출력
for day in range(1, num_days_in_month + 1):
    print(f'{day:2d} ({weekdays[(first_weekday + day - 1) % 7]}) ', end='')


    # month_days.append(day)
    month_days.append({'day': day, 'week': weekdays[(first_weekday + day - 1) % 7]})

    # 줄 바꿈 조건 설정
    if (first_weekday + day) % 7 == 0:
        print()


print()
print()
print(month_days)

# 개행 조절 변수
newline_count = 0
for month_day in month_days:
    print('month_day : ', month_day)

    newline_count += 1
    # 7번째부터 개행
    if newline_count % 7 == 0:
        print()