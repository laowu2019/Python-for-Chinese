# coding=UTF-8
import time, datetime

def 设置本地时间语言():
    import locale
    locale.setlocale(locale.LC_ALL, 'zh_CN.UTF-8') 

def 时间戳转换(时间戳):
    return time.localtime(时间戳)
时间戳 = time.time #返回1970年1月1日午夜到现在的秒数, 浮点数
def 当前时间():
    return 时间戳转换(时间戳())
def 当前年份():
    时间 = 当前时间()    
    return 时间.tm_year
def 当前月份():
    时间 = 当前时间()    
    return 时间.tm_mon
def 当前日子():
    时间 = 当前时间()    
    return 时间.tm_mday
def 当前小时():
    时间 = 当前时间()    
    return 时间.tm_hour
def 当前分钟():
    时间 = 当前时间()    
    return 时间.tm_min
def 当前秒数():
    时间 = 当前时间()    
    return 时间.tm_sec
def 当前周几():             # 一周中的第几日, 0-6, 0为周一
    时间 = 当前时间()    
    return 时间.tm_wday
def 当前年日():             # 一年中的第几日, 1-366
    时间 = 当前时间()    
    return 时间.tm_yday

def 时间格式化(格式, 时间):
    return time.strftime(格式, 时间)
def 反时间格式化(时间字符串, 格式):
    return time.strptime(时间字符串, 格式)

def 睡眠(秒数):
    time.sleep(秒数)

def 计算机时间():
    return time.perf_counter()


日期时间 = datetime.datetime  # 主要用于计算两个日期时间相差的天数和刨除整数天剩余的秒数

def 相差天数(日期时间1, 日期时间2):
    return (日期时间2 - 日期时间1).days

def 相差秒数(日期时间1, 日期时间2):
    return (日期时间2 - 日期时间1).seconds    
