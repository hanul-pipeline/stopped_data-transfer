import datetime
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

    cursor = conn.cursor()

    query = "Insert INTO gas_data VALUES(%s,%s,%s,%s,%s,%s)"
    values=(example['date'], example['time'], example['sensor_id'], example['sensor_type'], example['gas_value'])
    cursor.execute(query,values)

    conn.commit()

    # 연결 닫기
    cursor.close()
    conn.close()
