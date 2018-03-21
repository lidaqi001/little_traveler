import threading
import time
import random

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print ("开始线程：" + self.name)
        print_time(self.name, self.counter, 5)
        print ("退出线程：" + self.name)


def print_time(threadName, delay, counter):
    _str = 'runoob' + str(random.randint(0, 999))
    test1 = Test(name=_str)
    time.sleep(delay)
    test1.save()
    # print('插入数据：' + _str)
    print ("%s: %s" % ('插入数据：' + _str, time.ctime(time.time())))
    # while counter:
    #     if exitFlag:
    #         threadName.exit()
    #     time.sleep(delay)
    #     print ("%s: %s" % (threadName, time.ctime(time.time())))
    #     counter -= 1
