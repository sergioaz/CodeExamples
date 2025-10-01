import schedule
import time
import datetime
import threading

def do_long_work():
    """This is the actual function doing the heavy lifting."""
    print(f"Starting the long work in a thread... Time: {datetime.datetime.now().time()}\n")
    time.sleep(5)
    print(f"Finished the long work in a thread.   Time: {datetime.datetime.now().time()}")

def long_running_job_launcher():
    """
    This is the function that schedule calls.
    It just starts the thread and returns immediately.
    """
    thread = threading.Thread(target=do_long_work)
    thread.start()

def quick_job():
    print(f"--> Quick job running!                  Time: {datetime.datetime.now().time()}")

# Schedule the launcher function, not the work function directly
schedule.every(10).seconds.do(long_running_job_launcher)
schedule.every(2).seconds.do(quick_job)

print("Scheduler started with threading.")
while True:
    schedule.run_pending()
    time.sleep(1)