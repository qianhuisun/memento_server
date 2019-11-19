import threading
import time

def chi():
    print("%s 吃着火锅开始：" % time.ctime())
    time.sleep(1)
    print("%s 吃着火锅：涮羊肉" % time.ctime())
    time.sleep(1)
    print("%s 吃着火锅：涮牛肉" % time.ctime())
    time.sleep(1)
    print("%s 吃着火锅：贡丸" % time.ctime())
    time.sleep(1)
    print("%s 吃火锅结束！" % time.ctime())
def ting():
    print("%s 哼着小曲1！" % time.ctime())
    time.sleep(2)
    print("%s 哼着小曲2！" % time.ctime())
    time.sleep(2)
    print("%s 哼着小曲3！" % time.ctime())
    time.sleep(2)
    print("%s 哼着小曲4！" % time.ctime())
    time.sleep(2)
    print("%s 哼着小曲5！" % time.ctime())
    time.sleep(2)