# 若干函数汉化

from random import random

def 评估(*表达式):
    return eval(*表达式)

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

函数(甲, 乙):
    return 甲+乙
#显示(格式化输出("竞技分析开始, 共模拟{1}{0}局比赛", 3, 6))    