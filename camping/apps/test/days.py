from datetime import datetime, timedelta

# 현재 날짜 가져오기
current_date = datetime.now()

# 이번 달의 첫 번째 날 가져오기
first_day_of_month = current_date.replace(day=1)

# 이번 달의 마지막 날 가져오기
last_day_of_month = first_day_of_month.replace(month=first_day_of_month.month % 12 + 1, day=1) - timedelta(days=1)

# 이번 달의 모든 날짜 가져오기
all_days_of_month = [first_day_of_month + timedelta(days=i) for i in range((last_day_of_month - first_day_of_month).days + 1)]

# 결과 출력
print("이번 달의 첫 번째 날:", first_day_of_month.strftime("%Y-%m-%d"))
print("이번 달의 마지막 날:", last_day_of_month.strftime("%Y-%m-%d"))
print("이번 달의 모든 날짜:", [day.strftime("%Y-%m-%d") for day in all_days_of_month])





# 현재 날짜 가져오기
current_date = datetime.now()

# 현재 날짜의 요일 가져오기 (0: 월요일, 1: 화요일, ..., 6: 일요일)
weekday = current_date.weekday()

# 요일을 문자열로 변환
weekday_names = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
weekday_str = weekday_names[weekday]

# 결과 출력
print("오늘은 {}입니다.".format(weekday_str))