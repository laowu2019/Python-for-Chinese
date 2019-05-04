# coding=UTF-8
from 内置函数汉化 import *
from 内置类方法汉化 import *
from 可视化 import *


配置中文字体('SimHei')

图面(1)

x = 线性点(0, 2, 100)

子图(311)

绘图(x, x, 'bo', label = '线性')

子图(312)

绘图(x, x**2, 'k', label = '平方')

子图(313)
绘图(x, x**3, 'r--', label = '立方')

x轴标签('X 轴')
y轴标签('Y 轴')

标题("简单函数图像")

图例()

显示图形()
