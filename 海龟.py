from turtle import *
from 常量汉化 import *

自动 = 'auto'
用户 = 'user'
不调整 = 'noresize'

class 新海龟(Turtle):
    def 前进(实例, 距离):
        实例.forward(距离)
    def 后退(实例, 距离):
        实例.backward(距离)
    def 右转(实例, 角度):
        实例.right(角度)
    def 左转(实例, 角度):
        实例.left(角度)
    def 前往(实例, x, y = 空): # 若 y 为空, 则 x 须为二元数组
        实例.goto(x, y)
    def 设置x坐标(实例, x):
        实例.x坐标 = x
    def 设置y坐标(实例, y):
        实例.y坐标 = y
    def 设置朝向(实例, 角度):
        实例.setheading(角度)
    def 返回原点(实例):
        实例.home()
    def 画圆(实例, 半径, 范围 = 空, 步数 = 空):
        实例.circle(半径, 范围, 步数)
    def 画点(实例, 大小 = 空, *颜色):
        实例.dot(大小, *颜色)
    def 印章(实例):
        实例.stamp()
    def 清除印章(实例, 印章标识):
        实例.clearstamp(印章标识)
    def 清除多个印章(实例, n = 空):
        实例.clearstamps(n)
    def 撤销(实例):
        实例.undo()
    def 速度(实例, 速度 = 空):
        实例.speed(速度)
    def 位置(实例):
        实例.position()
    def 目标方向(实例, x, y = 空):
        实例.towards(x, y)
    def x坐标(实例):
        实例.xcor()
    def y坐标(实例):
        实例.ycor()
    def 朝向(实例):
        实例.heading()
    def 距离(实例, x, y = 空):
        实例.distance(x, y)
    def 设置圆度数(实例, 圆度数):
        实例.degrees(圆度数)
    def 弧度(实例):
        实例.radians()
    def 画笔落下(实例):
        实例.pendown()
    def 画笔抬起(实例):
        实例.penup()
    def 画笔粗细(实例, 粗细 = 空):
        实例.pensize()
    def 画笔(实例, 画笔 = 空, **画笔字典):
        实例.pen(画笔, **画笔字典)
    def 画笔是否落下(实例):
        实例.isdown()
    def 颜色(实例, *参数):
        实例.color(*参数)
    def 画笔颜色(实例, *参数):
        实例.pencolor(*参数)
    def 填充颜色(实例, *参数):
        实例.fillcolor(*参数)
    def 是否填充(实例):
        实例.filling()
    def 开始填充(实例):
        实例.begin_fill()
    def 结束填充(实例):
        实例.end_fill()
    def 重置(实例):
        实例.reset()
    def 清空(实例):
        实例.clear()
    def 书写(实例, 信息, 是否移动 = 否, 对齐 = 左, 字体 = ("Arial", 8, 正常)):
        实例.write(信息, 是否移动, 对齐, 字体)
    def 显示海龟(实例):
        实例.showturtle()
    def 隐藏海龟(实例):
        实例.hideturtle()
    def 是否可见(实例):
        实例.isvisible()
    def 形状(实例, 形状名称 = 空):
        实例.shape(形状名称)
    def 大小调整模式(实例, 调整模式 = 空):
        实例.resizemode(调整模式)
    def 形状大小(实例, 宽度伸缩因子 = 空, 长度伸缩因子 = 空, 轮廓宽度 = 空):
        实例.shapesize(宽度伸缩因子, 长度伸缩因子, 轮廓宽度)
    def 剪切因子(实例, 剪切因子 = 空):
        实例.shearfactor(剪切因子)
    def 设置倾角(实例, 倾角):
        实例.settiltangle(倾角)
    def 倾角(实例, 倾角 = 空):
        实例.tiltangle(倾角)
    def 倾斜(实例, 角度):
        实例.tilt(角度)
    def 变形(实例, t11 = 空, t12 = 空, t21 = 空, t22 = 空):
        实例.shapetransform(t11, t12, t21, t22)
    def 获取形状多边形(实例):
        实例.get_shapepoly()
    def 当点击鼠标(实例, 函数, 鼠标键 = 1, 增加 = 空):
        实例.onclick(函数, 鼠标键, 增加)
    def 当释放鼠标(实例, 函数, 鼠标键 = 1, 增加 = 空):
        实例.onrelease(函数, 鼠标键, 增加)
    def 当拖动鼠标(实例, 函数, 鼠标键 = 1, 增加 = 空):
        实例.ondrag(函数, 鼠标键, 增加)
    def 开始记录多边形(实例):
        实例.begin_poly()
    def 结束记录多边形(实例):
        实例.end_poly()
    def 获取多边形(实例):
        实例.get_poly()
    def 克隆(实例):        # 调用父类方法, 原问题已解决
        return Turtle.clone(实例)
    def 获取海龟(实例):
        实例.getturtle()
    def 获取屏幕(实例):
        实例.getscreen()
    def 设置撤消缓冲区(实例, 大小):
        实例.setundobuffer(大小)
    def 撤消缓冲区条目数(实例):
        实例.undobufferentries()
    """ def 背景颜色(实例):
        实例.bgcolor()
    def 背景图片(实例):
        实例.bgpic()
    def 屏幕大小(实例):
        实例.screensize()
    def 设置世界坐标系(实例):
        实例.setworldcoordinates()
    def 延迟(实例):
        实例.delay()
    def 轨迹(实例):
        实例.tracer()
    def 更新(实例):
        实例.update()
    def 监听(实例):
        实例.listen()
    def 当键盘按下并释放(实例):
        实例.onkey()
    def 当键盘按下(实例):
        实例.onkeypress()
    def 当点击屏幕(实例):
        实例.onclick()
    def 当达到定时(实例):
        实例.ontimer()
    def 完成(实例):
        实例.done()
    def 主循环(实例):
        实例.mainloop()
    def 模式(实例):
        实例.mode()
    def 颜色模式(实例):
        实例.colormode()
    def 获取画布(实例):
        实例.getcanvas()
    def 获取形状(实例):
        实例.getshapes()
    def 添加形状(实例):
        实例.register_shape()
    def 所有海龟(实例):
        实例.turtles()
    def 窗口高度(实例):
        实例.window_height()
    def 窗口宽度(实例):
        实例.window_width()
    def 文本输入(实例):
        实例.textinput()
    def 数字输入(实例):
        实例.numinput()
    def 再见(实例):
        实例.bye()
    def 当点击时退出(实例):
        实例.exitonclick()
    def 设置(实例):
        实例.setup()
    def 标题(实例):
        实例.title() """


# 海龟动作
#   移动和绘制
前进 = forward
后退 = backward
右转 = right
左转 = left
前往 = goto
设置x坐标 = setx
设置y坐标 = sety
设置朝向 = setheading
返回原点 = home
画圆 = circle
画点 = dot
印章 = stamp
清除印章 = clearstamp
清除多个印章 = clearstamps
撤消 = undo
速度 = speed
#   获取海龟状态
位置 = position
目标方向 = towards
x坐标 = xcor
y坐标 = ycor
朝向 = heading
距离 = distance
#   设置与度量单位
设置圆度数 = degrees
弧度 = radians

# 画笔控制
#   绘图状态
画笔落下 = pendown
画笔抬起 = penup
画笔粗细 = pensize
画笔 = pen
画笔是否落下 = isdown
#   颜色控制
颜色 = color
画笔颜色 = pencolor
填充颜色 = fillcolor
#   填充
是否填充 = filling
开始填充 = begin_fill
结束填充 = end_fill
#   更多绘图控制
重置 = reset
清空 = clear
书写 = write #内部形参无法汉化?


# 海龟状态
#   可见性
显示海龟 = showturtle
隐藏海龟 = hideturtle
是否可见 = isvisible
#   外观
形状 = shape
大小调整模式 = resizemode
形状大小 = shapesize
剪切因子 = shearfactor
设置倾角 = settiltangle
倾角 = tiltangle
倾斜 = tilt
变形 = shapetransform
获取形状多边形 = get_shapepoly

# 使用事件
当点击鼠标 = onclick
当释放鼠标 = onrelease
当拖动鼠标 = ondrag

# 特殊海龟方法
开始记录多边形 = begin_poly
结束记录多边形 = end_poly
获取多边形 = get_poly
# 克隆 = clone # 此方法克隆出的Turtle对象不支持汉化函数, 不要使用.
获取海龟 = getturtle
获取屏幕 = getscreen
设置撤消缓冲区 = setundobuffer
撤消缓冲区条目数 = undobufferentries

# 屏幕方法
#   窗口控制
背景颜色 = bgcolor
背景图片 = bgpic 
清屏 = clear
重置 = reset
屏幕大小 = screensize
设置世界坐标系 = setworldcoordinates
#   动画控制
延迟 = delay
轨迹 = tracer
更新 = update 
#   使用屏幕事件
监听 = listen
当键盘按下并释放 = onkey
当键盘按下 = onkeypress
当点击屏幕 = onclick
当达到定时 = ontimer
完成, 主循环 = done, mainloop
#   设置与特殊方法
模式 = mode
颜色模式 = colormode
获取画布 = getcanvas
获取形状 = getshapes
添加形状 = register_shape
所有海龟 = turtles
窗口高度 = window_height
窗口宽度 = window_width
#   输入方法
文本输入 = textinput
数字输入 = numinput
#   Screen 专有方法
再见 = bye
当点击时退出 = exitonclick
设置 = setup
标题 = title