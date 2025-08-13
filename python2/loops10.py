# implement an exponential backoff stretegy that doubles the wait time between retries ,starting from 1sec but stops after 5 retries

import time

wait_time = 1

max_retries = 5
attempts = 1

while attempts < max_retries:
    print(f"attempt {attempts} ~ wait time {wait_time}")
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
