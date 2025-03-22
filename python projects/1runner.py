import datetime as date
import time
is_running = True
def time_runner():
    while is_running:
        now = date.datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
        print("Welcome to the 1Runner program!")
        time.sleep(1)
time_runner()