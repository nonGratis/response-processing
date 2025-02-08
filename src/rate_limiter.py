import time
from collections import deque
from datetime import datetime, timedelta
import logging

class RateLimiter:
    def __init__(self, rpm_limit: int, tpm_limit: int, rpd_limit: int, tpd_limit: int):
        self.rpm_limit = rpm_limit
        self.tpm_limit = tpm_limit
        self.rpd_limit = rpd_limit
        self.tpd_limit = tpd_limit
        
        self.requests_minute = deque()
        self.tokens_minute = deque()
        self.requests_day = deque()
        self.tokens_day = deque()
    
    def _clean_old_entries(self, queue: deque, time_limit: timedelta):
        current_time = datetime.now()
        while queue and (current_time - queue[0][0]) > time_limit:
            queue.popleft()

    def check_limits(self, tokens: int) -> float:
        now = datetime.now()
        self._clean_old_entries(self.requests_minute, timedelta(minutes=1))
        self._clean_old_entries(self.tokens_minute, timedelta(minutes=1))
        self._clean_old_entries(self.requests_day, timedelta(days=1))
        self._clean_old_entries(self.tokens_day, timedelta(days=1))
        
        rpm_used = len(self.requests_minute)
        tpm_used = sum(t for _, t in self.tokens_minute)
        rpd_used = len(self.requests_day)
        tpd_used = sum(t for _, t in self.tokens_day)
        
        if (rpm_used >= self.rpm_limit or tpm_used + tokens > self.tpm_limit or 
            rpd_used >= self.rpd_limit or tpd_used + tokens > self.tpd_limit):
            logging.warning("Rate limit reached. Waiting for one minute.")
            return 60
        return 0

    def add_request(self, tokens: int):
        now = datetime.now()
        self.requests_minute.append((now, 1))
        self.tokens_minute.append((now, tokens))
        self.requests_day.append((now, 1))
        self.tokens_day.append((now, tokens))
