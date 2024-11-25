from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def get_week_days():
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
    week_days = [{'day': 0, 'week': '일'}]

    # 시작 요일 이전의 공백 출력
    for i in range(first_weekday):
        week_days.append({'day': 0, 'week': weekdays[i]})

    # 날짜와 요일 출력
    for day in range(1, num_days_in_month + 1):
        week_days.append({'day': day, 'week': weekdays[(first_weekday + day - 1) % 7]})

        # 줄 바꿈 조건 설정
        if (first_weekday + day) % 7 == 0:
            print()

    return week_days

def get_data():
    week_days = get_week_days()

    # 크롬 옵션 설정
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # headless 모드 설정

    # 크롬 드라이버 실행
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver = webdriver.Chrome(service=Service())

    url = "https://reserve.gmuc.co.kr/mobile/camp/campReservation.do?menu=d&menuFlag=C"
    driver.get(url)
    # # time.sleep(5)

    tr_elements = driver.find_elements(By.CSS_SELECTOR, '.trBefore')

    
    date_count = 0
    for tr_element in tr_elements:
        tds = tr_element.find_elements(By.TAG_NAME, 'td')

        for td in tds:
            if len(week_days) > date_count:
                # td 요소 안에 있는 모든 하위 요소들 찾기
                child_elements = td.find_elements(By.XPATH, ".//*")


                # 하위 요소들이 존재하는지 확인
                if len(child_elements) > 0:
                    # td 요소 안에 class가 'done'인 요소 찾기
                    done_elements = td.find_elements(By.CLASS_NAME, 'done')

                    if len(done_elements) > 0:
                        week_days[date_count]['STATUS'] = 'DONE'
                    else:
                        # week_days[date_count]['test'] = td.text
                        circle1 = td.find_element(By.CSS_SELECTOR, '.circle1 > a')
                        circle2 = td.find_element(By.CSS_SELECTOR, '.circle2 > a')

                        week_days[date_count]['STATUS'] = 'ING'
                        week_days[date_count]['A'] = circle1.text
                        week_days[date_count]['B'] = circle2.text

                else:
                    week_days[date_count]['STATUS'] = 'XXX'

            date_count += 1


    # WebDriver 종료
    driver.quit()

    return week_days

if __name__ == '__main__':
    datas = get_data()

    include_days = [25, 27]

    # 첫 번째 조건: STATUS가 'ING'이고 week이 '금', '토', '일'이며 'A' 또는 'B'가 0보다 큰 경우
    filtered_data1 = [item for item in datas if item.get('STATUS') == 'ING' and item.get('week') in ['금', '토', '일'] and (int(item.get('A', 0)) > 0 or int(item.get('B', 0)) > 0)]

    # 두 번째 조건: STATUS가 'ING'이고 day가 10, 20, 22이며 'A' 또는 'B'가 0보다 큰 경우
    filtered_data2 = [item for item in datas if item.get('STATUS') == 'ING' and item.get('day') in include_days and (int(item.get('A', 0)) > 0 or int(item.get('B', 0)) > 0)]

    if (filtered_data1 is not None and len(filtered_data1) > 0) or (filtered_data2 is not None and len(filtered_data2) > 0):
        print("있다.")
        print("filtered_data1 : ", filtered_data1)
        print("filtered_data2 : ", filtered_data2)

