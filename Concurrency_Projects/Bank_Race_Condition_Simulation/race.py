import threading
import time
balance = 1000
lock = threading.Lock()
def withdraw_without_lock(amount):
    global balance
    if balance >= amount:
        #temp = balance
        time.sleep(0.1)  
        #temp -= amount
        #balance = temp
        balance=balance-amount
        print(f"{threading.current_thread().name} withdrew {amount}. Balance: {balance}")
    else:
        print(f"{threading.current_thread().name} tried to withdraw but insufficient balance.")
        balance=temp
print("------ WITHOUT LOCK ------")
threads = []
for i in range(10):
    t = threading.Thread(target=withdraw_without_lock, args=(150,), name=f"Thread-{i+1}")
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print("Final Balance (Without Lock):", balance)
balance = 1000  
def withdraw_with_lock(amount):
    global balance
    with lock:  
        if balance >= amount:
            temp = balance
            time.sleep(0.1)
            temp -= amount
            balance = temp
            print(f"{threading.current_thread().name} withdrew {amount}. Balance: {balance}")
        else:
            print(f"{threading.current_thread().name} tried to withdraw but insufficient balance.")
print("\n------ WITH LOCK ------")
threads = []
for i in range(10):
    t = threading.Thread(target=withdraw_with_lock, args=(150,), name=f"Thread-{i+1}")
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print("Final Balance (With Lock):", balance)



# OUTPUT:
# ------ WITHOUT LOCK ------
# Thread-1 withdrew 150. Balance: 850
# Thread-2 withdrew 150. Balance: 700
# Thread-3 withdrew 150. Balance: 550
# Thread-5 withdrew 150. Balance: 400
# Thread-4 withdrew 150. Balance: 250
# Thread-7 withdrew 150. Balance: 100
# Thread-6 withdrew 150. Balance: -50
# Thread-8 withdrew 150. Balance: -200
# Thread-9 withdrew 150. Balance: -350
# Thread-10 withdrew 150. Balance: -500
# Final Balance (Without Lock): -500

# ------ WITH LOCK ------
# Thread-1 withdrew 150. Balance: 850
# Thread-2 withdrew 150. Balance: 700
# Thread-3 withdrew 150. Balance: 550
# Thread-4 withdrew 150. Balance: 400
# Thread-5 withdrew 150. Balance: 250
# Thread-6 withdrew 150. Balance: 100
# Thread-7 tried to withdraw but insufficient balance.
# Thread-8 tried to withdraw but insufficient balance.
# Thread-9 tried to withdraw but insufficient balance.
# Thread-10 tried to withdraw but insufficient balance.
# Final Balance (With Lock): 100
