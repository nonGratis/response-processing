import os
import time
from dotenv import load_dotenv
import openai
import logging
from typing import Optional
from config import *
from prompts import SYSTEM_PROMPT
from rate_limiter import RateLimiter

class GPTClient:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('GPT_API_KEY')
        if not self.api_key:
            raise ValueError("GPT API key not found in environment variables")
        openai.api_key = self.api_key
        self.client = openai.OpenAI(api_key=self.api_key)
        self.rate_limiter = RateLimiter(RPM_LIMIT, TPM_LIMIT, RPD_LIMIT, TPD_LIMIT)

    def get_response(self, prompt: str) -> Optional[str]:
        estimated_tokens = len(prompt.split()) + MAX_TOKENS
        wait_time = self.rate_limiter.check_limits(estimated_tokens)
        if wait_time > 0:
            time.sleep(wait_time)
        try:
            response = self.client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt}
                ],
                temperature=DEFAULT_TEMPERATURE,
                max_tokens=MAX_TOKENS
            )
            actual_tokens = response.usage.total_tokens
            self.rate_limiter.add_request(actual_tokens)
            return response.choices[0].message.content.strip()
        except Exception as e:
            logging.error(f"Error while getting response from GPT: {e}")
            return None
