#from random import random
from 函数汉化 import 显示, 评估, 输入, 随机数, 数据范围, 格式化输出

def 打印竞赛信息():
    显示("这个程序模拟两个选手甲和乙的某种竞技比赛")
    显示("程序运行需要甲和乙的能力值(以0到1之间的小数表示")

def 获取用户输入():
    甲能力值 = 评估(输入("请输入选手甲的能力值(0-1): "))
    乙能力值 = 评估(输入("请输入选手乙的能力值(0-1): "))
    总局数 = 评估(输入("模拟比赛的局数: "))
    return 甲能力值, 乙能力值, 总局数

def 打印结果(甲赢局数, 乙赢局数):
    总局数 = 甲赢局数 + 乙赢局数
    显示(格式化输出("竞技分析开始, 共模拟{}局比赛", 总局数))
    显示(格式化输出("选手甲获胜{}局, 占比{:0.1%}", 甲赢局数, 甲赢局数/总局数))
    显示(格式化输出("选手乙获胜{}局, 占比{:0.1%}", 乙赢局数, 乙赢局数/总局数))

def 一局游戏结束(甲得分, 乙得分):
    return 甲得分 == 15 or 乙得分 == 15

def 模拟一局游戏(甲能力值, 乙能力值):
    甲得分, 乙得分 = 0, 0
    发球方 = '甲'
    while not 一局游戏结束(甲得分, 乙得分):
        if 发球方 == '甲':
            if 随机数() < 甲能力值:
                甲得分 += 1
            else:
                发球方 = '乙'
        else:
            if 随机数() < 乙能力值:
                乙得分 += 1
            else:
                发球方 = '甲'
    return 甲得分, 乙得分

def 模拟游戏(总局数, 甲能力值, 乙能力值):
    甲赢局数, 乙赢局数 = 0, 0
    for 每一局 in 数据范围(总局数):
        甲得分, 乙得分 = 模拟一局游戏(甲能力值, 乙能力值)
        if 甲得分 > 乙得分:
            甲赢局数 += 1
        else:
            乙赢局数 += 1
    return 甲赢局数, 乙赢局数


def 主函数():
    打印竞赛信息()
    甲能力值, 乙能力值, 总局数 = 获取用户输入()
    甲赢局数, 乙赢局数 = 模拟游戏(总局数, 甲能力值, 乙能力值)
    打印结果(甲赢局数, 乙赢局数)

主函数()