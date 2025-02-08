import logging
import time
from pathlib import Path

import pandas as pd

from gpt_client import GPTClient
from prompts import *


class ResponseProcessor:
    def __init__(self, input_file: str, output_file: str):
        self.input_file = Path(input_file)
        self.output_file = Path(output_file)
        self.gpt_client = GPTClient()
        self._setup_logging()

    def _setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def _select_prompt(self, q_id: int):
        if q_id in [6, 11]:
            prompt = globals().get(f'Q_{q_id}')
        elif q_id in [18, 19]:
            prompt = Q_18
        else:
            return None
        return prompt + '\n\nВхідні дані для даного завдання: '

    def process(self):
        if not self.input_file.exists():
            logging.error(f'File {self.input_file} was not found!')
            return

        data = pd.read_csv(self.input_file, sep=';')
        results = []
        for _, row in data.iterrows():
            q_id = row['Q_ID']
            option = row['Option']
            prompt = self._select_prompt(q_id)
            response = self.gpt_client.get_response(prompt + option) if prompt else option
            if 'Вихід: ' in response:
                response = response.replace('Вихід: ', '')
            results.append({'R_ID': row['R_ID'], 'Q_ID': q_id, 'Option': option, 'Processed': response})

            output_df = pd.DataFrame(results)
            output_df.to_csv(self.output_file, sep=';', index=False)
            time.sleep(3)
