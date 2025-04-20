from datetime import datetime

WEATHER_PORT = 10100


def print_log(*args, sep=' ', end='\n', file=None):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]  # 格式化时间，保留到毫秒
    print(f'{current_time}', *args, sep=' ', end='\n', flush=True, file=file)