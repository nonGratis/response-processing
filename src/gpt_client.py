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
        self.client = openai.OpenAI(api_key=self.api_key)

    def get_response(self, prompt: str) -> Optional[str]:
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "system", "content": "Ви — інтелектуальний помічник з обробки даних, якому доручено очищати та структурувати відповіді на опитування для аналізу. Ваша мета — обробити необроблені вхідні дані та надати найбільш відповідний і структурований результат на основі попередньо визначених правил."},
                          {"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=150
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            logging.error(f"Error while getting response from GPT: {e}")
            return None

## model="gpt-4o-mini"
## temperature about 0.6-0.8
## max_tokens at least 100-150
