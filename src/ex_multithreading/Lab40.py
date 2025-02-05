import threading

x = 0

def increament():
    global x
    x += 1

def thread_task():

    for _ in range(100000):
        increament()

def main_task():
    global x
    x = 0

    t1 = threading.Thread(target=thread_task)
    t2 = threading.Thread(target=thread_task)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    for i in range(10):
        main_task()
        print("Iteration {0}: x = {1}".format(i,x))

# import threading
#
# x = 0
#
# def increament():
#     global x
#     x += 1
#
# def thread_task(lock):
#
#     for _ in range(100000):
#         lock.acquire()
#         increament()
#         lock.release()
#
# def main_task():
#     global x
#     x = 0
#
#     lock = threading.Lock()
#
#     t1 = threading.Thread(target=thread_task, args=(lock,))
#     t2 = threading.Thread(target=thread_task, args=(lock,))
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#
# if __name__ == '__main__':
#     for i in range(10):
#         main_task()
#         print("Iteration {0}:x = {1}".format(i,x))