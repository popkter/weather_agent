from datetime import datetime

WEATHER_PORT = 10100


def print_log(msg, end='\n'):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(sep=f'{time}: {msg} ', end=end, flush=True)
