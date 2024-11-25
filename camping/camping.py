
from apps.module import api
from apps.module import slack
import json

def main():
    datas = api.get_data()
    # print("datas : ", datas)

    include_days = [10, 30]

    # 첫 번째 조건: STATUS가 'ING'이고 week이 '금', '토', '일'이며 'A' 또는 'B'가 0보다 큰 경우
    filtered_data1 = [item for item in datas if item.get('STATUS') == 'ING' and item.get('week') in ['금', '토', '일'] and (int(item.get('A', 0)) > 0 or int(item.get('B', 0)) > 0)]

    # 두 번째 조건: STATUS가 'ING'이고 day가 10, 20, 22이며 'A' 또는 'B'가 0보다 큰 경우
    filtered_data2 = [item for item in datas if item.get('STATUS') == 'ING' and item.get('day') in include_days and (int(item.get('A', 0)) > 0 or int(item.get('B', 0)) > 0)]


    if (filtered_data1 is not None and len(filtered_data1) > 0) or (filtered_data2 is not None and len(filtered_data2) > 0):
        print("있다.")
        print("filtered_data1 : ", filtered_data1)
        print("filtered_data2 : ", filtered_data2)

    # Slack 메시지 전송
    if filtered_data1:
        filtered_data1_json = json.dumps(filtered_data1, ensure_ascii=False, indent=2)
        slack.send_message(filtered_data1_json)

    if filtered_data2:
        filtered_data2_json = json.dumps(filtered_data2, ensure_ascii=False, indent=2)
        slack.send_message(filtered_data2_json)


if __name__ == '__main__':
    main()