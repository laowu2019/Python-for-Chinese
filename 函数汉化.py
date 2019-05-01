# 若干函数汉化

from random import random

def 评估(表达式, *参数):
    return eval(表达式, *参数)

def 显示(*参数):
    print(*参数)

def 输入(*参数):
    字符串 = input(*参数)
    return 字符串

def 随机数(*参数):
    return random(*参数)

def 数据范围(*参数):
    return range(*参数)


def 格式化输出(字符串, *参数):
    return 字符串.format(*参数)

def 无操作():
    pass

def 执行(*参数):
    return exec(*参数)

是, 真 = True, True
否, 假 = False, False

def 退出():
    exit(0)

def 有错误退出():
    exit(1)


