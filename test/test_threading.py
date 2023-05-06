import threading
import time

def thread_job():
    for i in range(100):
        print(i)

def thread_add_num():
    for i in range(100):
        num = 1 + i
        print(num)
def main():
    add_thread = threading.Thread(target=thread_job)
    thread2 = threading.Thread(target=thread_add_num)

    add_thread.start()
    thread2.start()
    print(time.thread_time())
    print('正在跑：',threading.active_count())

'''
    print(threading.active_count())
    print(threading.enumerate())
    print(threading.current_thread())
'''

print(threading.active_count())
main()