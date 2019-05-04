import matplotlib.pyplot as plt
import numpy as np

图面 = plt.figure
子图 = plt.subplot
绘图 = plt.plot
轴域 = plt.axes
x轴标签 = plt.xlabel
y轴标签 = plt.ylabel
标题 = plt.title
图例 = plt.legend
文本 = plt.text
x轴刻度 = plt.xscale
y轴刻度 = plt.yscale
网格 = plt.grid
显示图形 = plt.show
清除当前图形 = plt.clf
清除当前轴域 = plt.cla
关闭图形 = plt.close
线性点 = np.linspace

def 配置中文字体(字体名称):
    from pylab import mpl
    mpl.rcParams['font.sans-serif'] = [字体名称]
    mpl.rcParams['axes.unicode_minus'] = False 
