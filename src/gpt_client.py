import os
from dotenv import load_dotenv
import openai
import logging
from typing import Optional
from config import *
from prompts import SYSTEM_PROMPT

class GPTClient:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('GPT_API_KEY')
        if not self.api_key:
            raise ValueError("GPT API key not found in environment variables")
        openai.api_key = self.api_key
        self.client = openai.OpenAI(api_key=self.api_key)

    def get_response(self, prompt: str) -> Optional[str]:
        try:
            response = self.client.chat.completions.create(
                model=MODEL_NAME,
                messages=[{"role": "system", "content": SYSTEM_PROMPT},
                          {"role": "user", "content": prompt}],
                temperature=DEFAULT_TEMPERATURE,
                max_tokens=MAX_TOKENS
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            logging.error(f"Error while getting response from GPT: {e}")
            return None
