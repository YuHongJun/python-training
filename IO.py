# from io import StringIO
#
# f = StringIO('Hello!\nHi!\nGoodbye!')
# while True:
#     s = f.readline()
#     if s == '':
#         break
#     print(s)

# 最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：
# import os
# [x for x in os.listdir('.') if os.path.isdir(x)]

# 要列出所有的.py文件，也只需一行代码：
# [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

#编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径
# import os
# def search(dir, text):
#     for x in os.listdir(dir):
#         if os.path.isfile(os.path.join(dir,x)):
#             if text in os.path.splitext(x)[0]:
#                 print('%s, %s'% (dir, x))
#         if os.path.isdir(os.path.join(dir,x)):
#             search(os.path.join(dir, x),text)
#
# print(os.path.abspath('.'))
# search('/Users/yuhongjun/reactNativeWorkSpace/YuHongJun.github.io' , 'feedtest2')
#
# import os
#
# print('Process (%s) start...' % os.getpid())
# # Only works on Unix/Linux/Mac:
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

# import subprocess
#
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code:', r)

# from multiprocessing import Process, Queue
# import os, time, random
#
# # 写数据进程执行的代码:
# def write(q):
#     print('Process to write: %s' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())
#
# # 读数据进程执行的代码:
# def read(q):
#     print('Process to read: %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)
#
# if __name__=='__main__':
#     # 父进程创建Queue，并传给各个子进程：
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # 启动子进程pw，写入:
#     pw.start()
#     # 启动子进程pr，读取:
#     pr.start()
#     # 等待pw结束:
#     pw.join()
#     # pr进程里是死循环，无法等待其结束，只能强行终止:
#     pr.terminate()

# import time, threading
#
# # 新线程执行的代码:
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)
#
# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)
#
# import time, threading
# balance = 0
# lock = threading.Lock()
#
# def change_it(n):
#     # 先存后取，结果应该为0:
#     global balance
#     balance = balance + n
#     balance = balance - n
#
# def run_thread(n):
#     for i in range(100000):
#         # 先要获取锁:
#         lock.acquire()
#         try:
#             # 放心地改吧:
#             change_it(n)
#         finally:
#             # 改完了一定要释放锁:
#             lock.release()

# import re
# re_mail=re.compile(r'^(.+)@([a-zA-Z0-9]+)\.([a-zA-Z0-9]{2,3}|[0-9]{1,3})$')
# a=re_mail.match('someone@gmail.com').groups()
# print(a)

# from datetime import datetime
# now=datetime.now()
# print(now)
# print(type(now))
#
# dt=datetime(2017,8,17,12,12)
# tt=dt.timestamp()
#
# print(datetime.fromtimestamp(tt)) # 本地时间
# print(datetime.utcfromtimestamp(tt)) # UTC时间

# from datetime import datetime
# cday = datetime.strptime('2017-8-17 12:12:12','%Y-%m-%d %H:%M:%S')
# print(cday)
#
# now=datetime.now()
# print(now.strftime('%a,%b %d %H:%M'))

import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    print(dt)
    tz_info = re.split(r'[UTC\:]+',tz_str)

    print(tz_info)
    tz_hours = int(tz_info[1])
    print(tz_hours)

    tz_minutes = int(tz_info[2])
    print(tz_minutes)

    dt = dt.replace(tzinfo = timezone(timedelta(hours=tz_hours, minutes=tz_minutes)))
    return dt.timestamp()

# 测试:

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('Pass')