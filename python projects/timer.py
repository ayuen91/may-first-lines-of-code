import time
def time_count(end, start=1):
    for i in range(end, start-1, -1):
        print(i)
        time.sleep(1)
    print("Time's up!")
time_count(10)