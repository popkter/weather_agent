from datetime import datetime
from pydantic import BaseModel, validator
from enum import Enum

WEATHER_PORT = 10100


def print_log(*args, sep=' ', end='\n', file=None):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]  # 格式化时间，保留到毫秒
    print(f'{current_time}', *args, sep=' ', end='\n', flush=True, file=file)


class WeatherEventType(str, Enum):
    days_detail = "days_detail"
    hours_detail = "hours_detail"
    summary = "summary"
    finish = "finish"
    error = "error"


class WeatherSseResponse(BaseModel):
    req_id: str
    type: WeatherEventType
    data: str

    def to_dict(self):
        return {'requestId': self.req_id, 'type': self.type.value, 'data': self.data}
