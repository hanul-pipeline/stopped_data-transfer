import datetime
import time

def gas_data(sensor_id,sensor_type,value):
    date_str = datetime.today().strftime("%Y-%m-%d")
    time_str = datetime.today().strftime("%H:%M:%S")

    example ={
        'date':date_str,
        "time":time_str,
        "sensor_id":sensor_id,
        "sensor_type":sensor_type,
        "gas_value":value
    }
    
    warning_flag = False  # 초기에 경고 플래그를 False로 설정
    start_time = None  # 가스 레벨이 범위에 들어간 시간을 추적

    while True:

        if example['gas_value'] < 12.8:
            if warning_flag:
                print("안전: 가스 레벨이 정상입니다.")
                warning_flag = False
            start_time = None  # 범위를 벗어나면 시간 초기화
        elif 12.8 <= example['gas_value'] <= 15.9:
            if not warning_flag:
                print("경고: 가스 레벨이 높습니다!")
                warning_flag = True
                start_time = time.time()  # 경고 플래그가 설정되면 시작 시간 설정
            elif time.time() - start_time >= 5:  # 경고 상태가 5초 이상 유지되면
                print("빨리 피신하세요: 가스 레벨이 매우 높습니다!")
        else:
            if warning_flag:
                print("빨리 피신하세요: 가스 레벨이 매우 높습니다!")
                warning_flag = False
            start_time = None  # 범위를 벗어나면 시간 초기화

        time.sleep(1)  # 1초마다 가스 레벨을 확인하도록 설정