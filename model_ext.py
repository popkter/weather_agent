import os
import asyncio
from typing import AsyncGenerator
from dotenv import load_dotenv
from openai import AsyncOpenAI
from function_call import weather_info_extract

load_dotenv()

MODEL_API_KEY = os.getenv("MODEL_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")
MODEL_FC_NAME = os.getenv("MODEL_FC_NAME")
MODEL_PATH = os.getenv("MODEL_PATH")

# 用于限制并发请求的信号量
SEMAPHORE = asyncio.Semaphore(10)

def create_client():
    return AsyncOpenAI(api_key=MODEL_API_KEY, base_url=MODEL_PATH, timeout=30.0)

async def llm_request(message, tool_call=weather_info_extract):
    client = create_client()
    async with SEMAPHORE:
        try:
            response = await client.chat.completions.create(
                model=MODEL_FC_NAME,
                messages=message,
                tools=tool_call
            )
            return response.choices[0].message
        except Exception as e:
            print(f"Error in llm_request: {str(e)}")
            raise

async def stream_llm_request(message) -> AsyncGenerator:
    client = create_client()
    async with SEMAPHORE:
        try:
            response = await client.chat.completions.create(
                model=MODEL_NAME,
                messages=message,
                stream=True
            )
            async for chunk in response:
                yield chunk
        except Exception as e:
            print(f"Error in stream_llm_request: {str(e)}")
            raise
