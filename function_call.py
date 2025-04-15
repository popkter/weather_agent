weather_info_extract = [
    {
        "type": "function",
        "function": {
            "name": "get_weather_range_days",
            "description": "获取某地指定时间段的天气，需要用户提供地点、起始日期、结束日期。如果查询的是今天的天气，请将起始日期和结束日期设置为今天。如果查询的是明天的天气请将起始日期和结束日期设为明天，如果查询的是三天内的天气，请将起始日期设置为今天，结束日期设置今天开始的第三天。其他情况请根据实际情况设置。如果查询的是下周的天气，请将起始日期设置为下周一",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "城市或者地点,如果是中国如上海市,需要转换为shanghai,如果美国如纽约市,需要转换为NewYork",
                    },
                    "start_date": {
                        "type": "string",
                        "description": "起始日期,格式为YYYY-MM-DD,",
                    },
                    "end_date": {
                        "type": "string",
                        "description": "结束日期,格式为YYYY-MM-DD,",
                    }
                },
                "required": ["location"]
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_weather_today_hours",
            "description": "获取某地某天每个小时的天气，需要用户提供地点、查询日期",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "城市或者地点,如果是中国如上海市,需要转换为shanghai,如果美国如纽约市,需要转换为NewYork",
                    },
                    "start_date": {
                        "type": "string",
                        "description": "查询日期,格式为YYYY-MM-DD,",
                    },
                },
                "required": ["location"]
            },
        }
    },
]
