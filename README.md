# VSC_Weather_Api

> customize api by deepseek & visual_crossing_weather for sample development

**基于deepseek api和visual_crossing_weather封装的在线天气查询总结服务**

## 部署

1. 克隆仓库到本地，运行main.py即可本地运行
2. 基于DockFile可构建自定义的docker镜像，按需选择暴露端口

## 使用

1. 使用Post请求

> 可查询最近一段时间和某天某时刻的天气，返回结果会先返回查询的天气信息，然后流式返回总结数据。

> 请求地址
>
> http://localhost:10011/query_weather
>
> Header
>
> > VisualCrossingWebServices获取的apikey
> ```json
> {
>   "Authorization":"Bearer 3JM2P466TENUYT8x1231aasdaza"
> }
> ```
> 请求体
>
> ```json
> {
>     "user_query":"上海市明天的天气怎么样"
> }
> ```

2. 根据输入query的不同，返回的数据结构也会有所不同。

- 查询一段日期

```json
{
  "type": "weather_data_days",
  "data": "[{\"date\": \"2024-11-29\", \"temperature\": {\"max\": 14.6, \"min\": 8.4, \"avg\": 11.3}, \"windspeed\": 23.4, \"conditions\": \"Clear\", \"humidity\": 28.4}]"
}
{
  "type": "summary",
  "data": "明天"
}
{
  "type": "summary",
  "data": "上海市"
}
{
  "type": "summary",
  "data": "天气"
}
{
  "type": "summary",
  "data": "晴"
}
{
  "type": "summary",
  "data": "朗"
}
{
  "type": "summary",
  "data": "，"
}
{
  "type": "summary",
  "data": "最高"
}
{
  "type": "summary",
  "data": "气温"
}
{
  "type": "summary",
  "data": "1"
}
{
  "type": "summary",
  "data": "4"
}
{
  "type": "summary",
  "data": "."
}
{
  "type": "summary",
  "data": "6"
}
{
  "type": "summary",
  "data": "℃"
}
{
  "type": "summary",
  "data": "，"
}
{
  "type": "summary",
  "data": "最低"
}
{
  "type": "summary",
  "data": "气温"
}
{
  "type": "summary",
  "data": "8"
}
{
  "type": "summary",
  "data": "."
}
{
  "type": "summary",
  "data": "4"
}
{
  "type": "summary",
  "data": "℃"
}
{
  "type": "summary",
  "data": "，"
}
{
  "type": "summary",
  "data": "平均"
}
{
  "type": "summary",
  "data": "气温"
}
{
  "type": "summary",
  "data": "1"
}
{
  "type": "summary",
  "data": "1"
}
{
  "type": "summary",
  "data": "."
}
{
  "type": "summary",
  "data": "3"
}
{
  "type": "summary",
  "data": "℃"
}
{
  "type": "summary",
  "data": "，"
}
{
  "type": "summary",
  "data": "风"
}
{
  "type": "summary",
  "data": "速"
}
{
  "type": "summary",
  "data": "适"
}
{
  "type": "summary",
  "data": "中"
}
{
  "type": "summary",
  "data": "，"
}
{
  "type": "summary",
  "data": "湿度"
}
{
  "type": "summary",
  "data": "较低"
}
{
  "type": "summary",
  "data": "，"
}
{
  "type": "summary",
  "data": "适合"
}
{
  "type": "summary",
  "data": "出游"
}
{
  "type": "summary",
  "data": "，"
}
{
  "type": "summary",
  "data": "但"
}
{
  "type": "summary",
  "data": "早晚"
}
{
  "type": "summary",
  "data": "温"
}
{
  "type": "summary",
  "data": "差"
}
{
  "type": "summary",
  "data": "较大"
}
{
  "type": "summary",
  "data": "，"
}
{
  "type": "summary",
  "data": "建议"
}
{
  "type": "summary",
  "data": "添加"
}
{
  "type": "summary",
  "data": "衣物"
}
{
  "type": "summary",
  "data": "注意"
}
{
  "type": "summary",
  "data": "防"
}
{
  "type": "summary",
  "data": "寒"
}
{
  "type": "summary",
  "data": "保暖"
}
{
  "type": "summary",
  "data": "。"
}
{
  "type": "finish",
  "data": true
}
```

- 查询指定时间

```json
{
  "type": "weather_data_hours",
  "data": "[{\"datetime\": \"00:00:00\", \"temp\": 8.0, \"feelslike\": 6.0, \"windspeed\": 10.8, \"humidity\": 38.82, \"conditions\": \"Clear\", \"uvindex\": 0.0, \"visibility\": 10.0}, {\"datetime\": \"01:00:00\", \"temp\": 6.1, \"feelslike\": 4.5, \"windspeed\": 7.9, \"humidity\": 47.41, \"conditions\": \"Clear\", \"uvindex\": 0.0, \"visibility\": 10.0}, {\"datetime\": \"02:00:00\", \"temp\": 6.1, \"feelslike\": 4.5, \"windspeed\": 7.9, \"humidity\": 51.09, \"conditions\": \"Clear\", \"uvindex\": 0.0, \"visibility\": 10.0}, {\"datetime\": \"03:00:00\", \"temp\": 6.0, \"feelslike\": 3.5, \"windspeed\": 11.5, \"humidity\": 55.73, \"conditions\": \"Clear\", \"uvindex\": 0.0, \"visibility\": 10.0}, {\"datetime\": \"04:00:00\", \"temp\": 5.6, \"feelslike\": 2.7, \"windspeed\": 13.7, \"humidity\": 61.53, \"conditions\": \"Clear\", \"uvindex\": 0.0, \"visibility\": 10.0}, {\"datetime\": \"05:00:00\", \"temp\": 5.0, \"feelslike\": 1.9, \"windspeed\": 13.7, \"humidity\": 61.37, \"conditions\": \"Clear\", \"uvindex\": 0.0, \"visibility\": 10.0}, {\"datetime\": \"06:00:00\", \"temp\": 5.0, \"feelslike\": 3.0, \"windspeed\": 8.5, \"humidity\": 57.78, \"conditions\": \"Clear\", \"uvindex\": 0.0, \"visibility\": 10.0}, {\"datetime\": \"07:00:00\", \"temp\": 6.0, \"feelslike\": 3.0, \"windspeed\": 14.4, \"humidity\": 52.46, \"conditions\": \"Clear\", \"uvindex\": 0.0, \"visibility\": 10.0}, {\"datetime\": \"08:00:00\", \"temp\": 8.0, \"feelslike\": 5.0, \"windspeed\": 18.0, \"humidity\": 43.03, \"conditions\": \"Clear\", \"uvindex\": 1.0, \"visibility\": 10.0}, {\"datetime\": \"09:00:00\", \"temp\": 10.0, \"feelslike\": 7.2, \"windspeed\": 21.6, \"humidity\": 37.6, \"conditions\": \"Clear\", \"uvindex\": 3.0, \"visibility\": 10.0}, {\"datetime\": \"10:00:00\", \"temp\": 12.0, \"feelslike\": 12.0, \"windspeed\": 20.0, \"humidity\": 32.03, \"conditions\": \"Clear\", \"uvindex\": 5.0, \"visibility\": 10.0}, {\"datetime\": \"11:00:00\", \"temp\": 13.8, \"feelslike\": 13.8, \"windspeed\": 27.2, \"humidity\": 28.44, \"conditions\": \"Clear\", \"uvindex\": 6.0, \"visibility\": 10.0}, {\"datetime\": \"12:00:00\", \"temp\": 14.0, \"feelslike\": 14.0, \"windspeed\": 29.5, \"humidity\": 24.84, \"conditions\": \"Clear\", \"uvindex\": 6.0, \"visibility\": 10.0}, {\"datetime\": \"13:00:00\", \"temp\": 14.1, \"feelslike\": 14.1, \"windspeed\": 33.1, \"humidity\": 21.05, \"conditions\": \"Clear\", \"uvindex\": 6.0, \"visibility\": 10.0}, {\"datetime\": \"14:00:00\", \"temp\": 14.1, \"feelslike\": 14.1, \"windspeed\": 35.3, \"humidity\": 22.11, \"conditions\": \"Clear\", \"uvindex\": 5.0, \"visibility\": 10.0}, {\"datetime\": \"15:00:00\", \"temp\": 14.0, \"feelslike\": 14.0, \"windspeed\": 34.4, \"humidity\": 24.16, \"conditions\": \"Clear\", \"uvindex\": 4.0, \"visibility\": 10.0}, {\"datetime\": \"16:00:00\", \"temp\": 13.0, \"feelslike\": 13.0, \"windspeed\": 30.8, \"humidity\": 25.07, \"conditions\": \"Clear\", \"uvindex\": 2.0, \"visibility\": 10.0}, {\"datetime\": \"17:00:00\", \"temp\": 12.0, \"feelslike\": 12.0, \"windspeed\": 28.8, \"humidity\": 23.94, \"conditions\": \"Clear\", \"uvindex\": 0.0, \"visibility\": 10.0}, {\"datetime\": \"18:00:00\", \"temp\": 11.1, \"feelslike\": 11.1, \"windspeed\": 20.5, \"humidity\": 25.01, \"conditions\": \"Clear\", \"uvindex\": 0.0, \"visibility\": 24.1}, {\"datetime\": \"19:00:00\", \"temp\": 10.7, \"feelslike\": 10.7, \"windspeed\": 19.4, \"humidity\": 24.9, \"conditions\": \"Clear\", \"uvindex\": 0.0, \"visibility\": 24.1}, {\"datetime\": \"20:00:00\", \"temp\": 10.2, \"feelslike\": 10.2, \"windspeed\": 19.1, \"humidity\": 26.35, \"conditions\": \"Clear\", \"uvindex\": 0.0, \"visibility\": 24.1}, {\"datetime\": \"21:00:00\", \"temp\": 9.8, \"feelslike\": 7.2, \"windspeed\": 18.7, \"humidity\": 25.83, \"conditions\": \"Clear\", \"uvindex\": 0.0, \"visibility\": 24.1}, {\"datetime\": \"22:00:00\", \"temp\": 9.5, \"feelslike\": 7.0, \"windspeed\": 17.3, \"humidity\": 25.95, \"conditions\": \"Clear\", \"uvindex\": 0.0, \"visibility\": 24.1}, {\"datetime\": \"23:00:00\", \"temp\": 9.2, \"feelslike\": 6.8, \"windspeed\": 15.8, \"humidity\": 27.1, \"conditions\": \"Clear\", \"uvindex\": 0.0, \"visibility\": 24.1}]"
}
{
  "type": "summary",
  "data": "今晚"
}
{
  "type": "summary",
  "data": "上海市"
}
{
  "type": "summary",
  "data": "天气"
}
{
  "type": "summary",
  "data": "晴"
}
{
  "type": "summary",
  "data": "朗"
}
{
  "type": "summary",
  "data": "，"
}
{
  "type": "summary",
  "data": "温度"
}
{
  "type": "summary",
  "data": "逐渐"
}
{
  "type": "summary",
  "data": "下降"
}
{
  "type": "summary",
  "data": "，"
}
{
  "type": "summary",
  "data": "从"
}
{
  "type": "summary",
  "data": "8"
}
{
  "type": "summary",
  "data": "."
}
{
  "type": "summary",
  "data": "0"
}
{
  "type": "summary",
  "data": "°"
}
{
  "type": "summary",
  "data": "C"
}
{
  "type": "summary",
  "data": "降至"
}
{
  "type": "summary",
  "data": "9"
}
{
  "type": "summary",
  "data": "."
}
{
  "type": "summary",
  "data": "2"
}
{
  "type": "summary",
  "data": "°"
}
{
  "type": "summary",
  "data": "C"
}
{
  "type": "summary",
  "data": "，"
}
{
  "type": "summary",
  "data": "风"
}
{
  "type": "summary",
  "data": "速"
}
{
  "type": "summary",
  "data": "适"
}
{
  "type": "summary",
  "data": "中"
}
{
  "type": "summary",
  "data": "，"
}
{
  "type": "summary",
  "data": "湿度"
}
{
  "type": "summary",
  "data": "较低"
}
{
  "type": "summary",
  "data": "，"
}
{
  "type": "summary",
  "data": "适合"
}
{
  "type": "summary",
  "data": "户外"
}
{
  "type": "summary",
  "data": "活动"
}
{
  "type": "summary",
  "data": "。"
}
{
  "type": "summary",
  "data": "建议"
}
{
  "type": "summary",
  "data": "适当"
}
{
  "type": "summary",
  "data": "添加"
}
{
  "type": "summary",
  "data": "衣物"
}
{
  "type": "summary",
  "data": "以防"
}
{
  "type": "summary",
  "data": "寒"
}
{
  "type": "summary",
  "data": "。"
}
{
  "type": "finish",
  "data": true
}
```

