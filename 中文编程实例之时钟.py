# coding=utf-8
import 海龟
from 内置函数汉化 import *
from 常量汉化 import *
from 时间日期汉化 import *
 
# 抬起画笔，向前运动一段距离放下
def 跳过(步数):
    海龟.画笔抬起()
    海龟.前进(步数)
    海龟.画笔落下()
 
def 绘制指针(名称, 长度):
    # 注册海龟形状，建立指针海龟
    海龟.重置()
    跳过(-长度 * 0.1)
    # 开始记录多边形的顶点。当前的乌龟位置是多边形的第一个顶点。
    海龟.开始记录多边形()
    海龟.前进(长度 * 1.1)
    # 停止记录多边形的顶点。当前的乌龟位置是多边形的最后一个顶点。将与第一个顶点相连。
    海龟.结束记录多边形()
    # 返回最后记录的多边形。
    指针形状 = 海龟.获取多边形()
    海龟.添加形状(名称, 指针形状)
 
def 初始化():
    global 秒针, 分针, 时针, 打印器
    # 重置海龟指向北
    海龟.模式("logo")
    # 建立三个表针海龟并初始化
    绘制指针("秒针", 135)
    绘制指针("分针", 125)
    绘制指针("时针", 90)
    秒针 = 海龟.新海龟()
    秒针.形状("秒针")
    分针 = 海龟.新海龟()
    分针.形状("分针")
    时针 = 海龟.新海龟()
    时针.形状("时针")
   
    for 指针 in 秒针, 分针, 时针:
        指针.形状大小(1, 1, 3)
        指针.速度(0)
   
    # 建立输出文字海龟
    打印器 = 海龟.新海龟()
    # 隐藏画笔的海龟形状
    打印器.隐藏海龟()
    打印器.画笔抬起()
    
def 设置时钟(半径):
    # 建立表的外框
    海龟.重置()
    海龟.画笔粗细(7)
    for i in 范围(60):
        跳过(半径)
        if i % 5 == 0:
            海龟.前进(20)
            跳过(-半径 - 20)
           
            跳过(半径 + 20)
            if i == 0:
                海龟.书写(int(12), align = 居中, font = ("Courier", 14, 粗体))
            elif i == 30:
                跳过(25)
                海龟.书写(int(i/5), align = 居中, font = ("Courier", 14, 粗体))
                跳过(-25)
            elif (i == 25 or i == 35):
                跳过(20)
                海龟.书写(int(i/5), align = 居中, font = ("Courier", 14, 粗体))
                跳过(-20)
            else:
                海龟.书写(int(i/5), align = 居中, font = ("Courier", 14, 粗体))
            跳过(-半径 - 20)
        else:
            海龟.画点(5)
            跳过(-半径)
        海龟.右转(6)
        
def 一周(第几天):   
    一周 = ["星期一", "星期二", "星期三",
            "星期四", "星期五", "星期六", "星期日"]
    return 一周[第几天]
 
def 日期():
    年 = 当前年份() #时间.year
    月 = 当前月份() #时间.month
    日 = 当前日子() #时间.day
    return "%s %d %d" % (年, 月, 日)
 
def 滴答():
    # 绘制表针的动态显示, 用datetime库实现的话, 秒钟运动更平滑
    #时间 = datetime.datetime.today()
    秒 = 当前秒数() #时间.second + 时间.microsecond * 0.000001
    分 = 当前分钟() #时间.minute + 秒 / 60.0
    时 = 当前小时() #时间.hour + 分 / 60.0
    秒针.设置朝向(6 * 秒)
    分针.设置朝向(6 * 分)
    时针.设置朝向(30 * 时)
    
    海龟.轨迹(否) 
    打印器.前进(65)
    打印器.书写(一周(当前周日()), 对齐 = 居中, 字体 = ("Courier", 14, 粗体))
    打印器.后退(130)
    打印器.书写(日期(), 对齐 = 居中, 字体 = ("Courier", 14, 粗体))
    打印器.返回原点()
    海龟.轨迹(是)
 
    # 100ms后继续调用tick
    海龟.当达到定时(滴答, 1000)
 
def 主函数():
    # 打开/关闭龟动画，并为更新图纸设置延迟。
    海龟.轨迹(否)
    初始化()
    设置时钟(160)
    海龟.轨迹(是)
    滴答()
    海龟.主循环()
 
if __name__ == "__main__":
    主函数()