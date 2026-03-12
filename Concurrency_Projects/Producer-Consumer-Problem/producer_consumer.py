import threading
import queue
import time
log_queue = queue.Queue(maxsize=5)
TOTAL_LOGS = 10
def producer():
    for i in range(1, TOTAL_LOGS + 1):
        log_message = f"Log{i}"
        log_queue.put(log_message)  
        print("Produced:", log_message)
        time.sleep(1)
    print("Producer finished producing logs")
def consumer():
    for i in range(TOTAL_LOGS):
        log_message = log_queue.get()  
        print("Consumed:", log_message)
        time.sleep(2)
        log_queue.task_done()
    print("Consumer finished processing logs")
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)
producer_thread.start()
consumer_thread.start()
producer_thread.join()
consumer_thread.join()
print("Program finished")


# OUTPUT:
# Produced: Log1
# Consumed: Log1
# Produced: Log2
# Consumed: Log2
# Produced: Log3
# Produced: Log4
# Consumed: Log3
# Produced: Log5
# Produced: Log6
# Consumed: Log4
# Produced: Log7
# Produced: Log8
# Consumed: Log5
# Produced: Log9
# Produced: Log10
# Consumed: Log6
# Producer finished producing logs
# Consumed: Log7
# Consumed: Log8
# Consumed: Log9
# Consumed: Log10
# Consumer finished processing logs
# Program finished
