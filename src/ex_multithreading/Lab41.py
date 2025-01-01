# import threading
#
# def print_cube(num):
#     print("cube : {}".format(num * num * num))
#
# def print_square(num):
#     print("square : {}".format(num * num))
#
# if __name__ == "__main__":
#     t1 = threading.Thread(target=print_cube, args=(10,))
#     t2 = threading.Thread(target=print_square, args=(10,))
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#
#     print("Done!")

import threading
import os

def task1():
    print("Thread running task1: {}".format(threading.current_thread().name))
    print("ID of process running task2: {}".format(os.getpid()))

def task2():
    print("Thread running task2: {}".format(threading.current_thread().name))
    print("ID of process running task2: {}".format(os.getpid()))

if __name__ == "__main__":
    print("ID of process running main programme: {}".format(os.getpid()))
    print("Main thread name: {}".format(threading.current_thread().name))

    t1 = threading.Thread(target=task1, name="t1")
    t2 = threading.Thread(target=task2, name="t2")

    t1.start()
    t2.start()

    t1.join()
    t2.join()