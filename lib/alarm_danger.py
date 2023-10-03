import datetime
import time


# 값 측정 함수, 위험 임계값, 측정 주기, 경과 시간 임계값, 대처 함수
def detect_single_measurement(measure_function,
                              danger_threshold, 
                              duration,
                                elapsed_threshold,
                                react_function):

    start_time = None
    danger_detected = False

    try:
        while True:
            start_measurement_time = time.time()

            measurement = measure_function()
            if measurement > danger_threshold:
                if not danger_detected:
                    start_time = time.time()
                    danger_detected = True
                else:
                    elapsed_time = time.time() - start_time
                    if elapsed_time >= elapsed_threshold:
                        react_function
            else:
                danger_detected = False
                start_time = None

            elapsed_measurement_time = time.time() - start_measurement_time
            remaining_time = duration - elapsed_measurement_time
            if remaining_time > 0:
                time.sleep(remaining_time)

    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    detect_single_measurement()