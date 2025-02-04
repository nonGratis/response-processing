import os
from dotenv import load_dotenv
import openai
import logging
from typing import Optional

class GPTClient:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('GPT_API_KEY')
        if not self.api_key:
            raise ValueError("GPT API key not found in environment variables")
        openai.api_key = self.api_key

