import os

from dotenv import load_dotenv
from openai import OpenAI

from function_call import weather_info_extract

load_dotenv()

MODEL_API_KEY = os.getenv("MODEL_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")
MODEL_FC_NAME = os.getenv("MODEL_FC_NAME")

MODEL_PATH = os.getenv("MODEL_PATH")

client = OpenAI(api_key=MODEL_API_KEY, base_url=MODEL_PATH)
fc_client = OpenAI(api_key=MODEL_API_KEY, base_url=MODEL_PATH)


def llm_request(message, tool_call=weather_info_extract):
    response = client.chat.completions.create(
        model=MODEL_FC_NAME,
        messages=message,
        tools=tool_call
    )
    return response.choices[0].message


def stream_llm_request(message):
    return client.chat.completions.create(
        model=MODEL_NAME,
        messages=message,
        stream=True
    )
    #
    #
    # for chunk in response:
    #     if not chunk.choices:
    #         continue
    #     print(chunk.choices[0].delta.content, end="")
    # print()
