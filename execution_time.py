import time
from time import strftime
from time import gmtime


def start_time_():
    start_time = time.time()
    return start_time


def end_time_():
    end_time = time.time()
    return end_time


def Execution_time():
    return strftime("%H:%M:%S", gmtime(int('{:.0f}'.format(float(str((end_time - start_time)))))))


start_time = start_time_()
# [i for i in range(0, 100000000)]
end_time = end_time_()
print("Execution_time is :", Execution_time())
