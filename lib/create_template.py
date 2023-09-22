'''
1. 시스템에 문제가 발생하여 데이터 관련 로직이 정상 동작하지 않을 경우 : 주어진 데이터만으로 위기 상황 판단이 가능해야 한다
2. 

'''


# 데이터 전송용 템플릿
# 센서 ID, 센서 이름, 분류, 측정 주기, 측정값, 현재 시간
def template_transfer(sensor_id, sensor_name, sensor_type, frequency, measurement):
    from datetime import datetime

    nowdate = datetime.now().strftime("%Y-%m-%d")
    nowtime = datetime.now().strftime("%H:%M:%S")

    template = {
        "sensor_id" : sensor_id,
        "sensor_name" : sensor_name,
        "sensor_type" : sensor_type,
        "frequency" : frequency,
        "measurement" : measurement,
        "date" : nowdate,
        "time" : nowtime
    }

    return template


# 위험 상황용 템플릿
# 위치 ID, 위치 이름, 위험 분류, 위험 단계, 대응, 경과 시간, 현재 시간
def template_warning():
    from datetime import datetime

    nowdate = datetime.now().strftime("%Y-%m-%d")
    nowtime = datetime.now().strftime("%H:%M:%S")
