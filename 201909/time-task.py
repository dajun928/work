#-*- conding:utf-8 -*-
''''''
'''
1.将字符串的时间"2017-10-10 23:40:00"转换为时间戳和时间元组

2.字符串格式更改。如提time = "2017-10-10 23:40:00",想改为 time= "2017/10/10 23:40:00"

3.获取当前时间戳转换为指定格式日期

4.获得三天前的时间

'''
import time


'''
times = "2017-10-10 23:40:00"
#将字符串时间转换为时间元祖
formatTime = time.strptime(times,'%Y-%m-%d %H:%M:%S')
print(formatTime)
#将时间元组转换为时间错
print(time.mktime(formatTime))
'''

'''
times = "2017-10-10 23:40:00"
formatTime = time.strptime(times,'%Y-%m-%d %H:%M:%S')
print(time.strftime('%Y/%m/%d %H:%M:%S',formatTime))
'''

# now = time.time()
# formatTime = time.localtime(now)

# threeAgo = time.time() - 60*60*24*3
# formatTime = time.localtime(threeAgo)
# print(time.strftime('%Y-%m-%d %H:%M:%S',formatTime))