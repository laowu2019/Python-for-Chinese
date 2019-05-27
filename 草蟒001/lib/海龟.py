from turtle import *

自动 = 'auto'
用户 = 'user'
不调整 = 'noresize'
红 = 'red'
黄 = 'yellow'
蓝 = 'blue'
黑 = 'black'
白 = 'white'
绿 = 'green'
左 = 'left'
右 = 'right'
居中 = 'center'
正常 = 'normal'
斜体 = 'italic'
粗体 = 'bold'
方形 = 'square'
点 = 'dot'
假 = False
真 = True

class 新海龟(Turtle):
    def 前进(自己, 距离):
        自己.forward(距离)
    def 后退(自己, 距离):
        自己.backward(距离)
    def 右转(自己, 角度):
        自己.right(角度)
    def 左转(自己, 角度):
        自己.left(角度)
    def 前往(自己, x, y = None): # 若 y 为None, 则 x 须为二元数组
        自己.goto(x, y)
    def 设置x坐标(自己, x):
        自己.x坐标 = x
    def 设置y坐标(自己, y):
        自己.y坐标 = y
    def 设置朝向(自己, 角度):
        自己.setheading(角度)
    def 返回原点(自己):
        自己.home()
    def 画圆(自己, 半径, 范围 = None, 步数 = None):
        自己.circle(半径, 范围, 步数)
    def 画点(自己, 大小 = None, *颜色):
        自己.dot(大小, *颜色)
    def 印章(自己):
        自己.stamp()
    def 清除印章(自己, 印章标识):
        自己.clearstamp(印章标识)
    def 清除多个印章(自己, n = None):
        自己.clearstamps(n)
    def 撤销(自己):
        自己.undo()
    def 速度(自己, 速度 = None):
        自己.speed(速度)
    def 位置(自己):
        return 自己.position()
    def 目标方向(自己, x, y = None):
        return 自己.towards(x, y)
    def x坐标(自己):
        return 自己.xcor()
    def y坐标(自己):
        return 自己.ycor()
    def 朝向(自己):
        return 自己.heading()
    def 距离(自己, x, y = None):
        return 自己.distance(x, y)
    def 设置圆度数(自己, 圆度数):
        自己.degrees(圆度数)
    def 弧度(自己):
        自己.radians()
    def 画笔落下(自己):
        自己.pendown()
    def 画笔抬起(自己):
        自己.penup()
    def 画笔粗细(自己, 粗细 = None):
        自己.pensize()
    def 画笔(自己, 画笔 = None, **画笔字典):
        return 自己.pen(画笔, **画笔字典)
    def 画笔是否落下(自己):
        return 自己.isdown()
    def 颜色(自己, *参数):
        return 自己.color(*参数)
    def 画笔颜色(自己, *参数):
        return 自己.pencolor(*参数)
    def 填充颜色(自己, *参数):
        return 自己.fillcolor(*参数)
    def 是否在填充(自己):
        return 自己.filling()
    def 开始填充(自己):
        自己.begin_fill()
    def 结束填充(自己):
        自己.end_fill()
    def 重置(自己):
        自己.reset()
    def 清None(自己):
        自己.clear()
    def 书写(自己, 信息, 是否移动 = 假, 对齐 = 左, 字体 = ("Arial", 8, 正常)):
        自己.write(信息, 是否移动, 对齐, 字体)
    def 显示海龟(自己):
        自己.showturtle()
    def 隐藏海龟(自己):
        自己.hideturtle()
    def 是否可见(自己):
        return 自己.isvisible()
    def 形状(自己, 形状名称 = None):
        自己.shape(形状名称)
    def 大小调整模式(自己, 调整模式 = None):
        自己.resizemode(调整模式)
    def 形状大小(自己, 宽度伸缩因子 = None, 长度伸缩因子 = None, 轮廓宽度 = None):
        return 自己.shapesize(宽度伸缩因子, 长度伸缩因子, 轮廓宽度)
    def 剪切因子(自己, 剪切因子 = None):
        return 自己.shearfactor(剪切因子)
    def 设置倾角(自己, 倾角):
        自己.settiltangle(倾角)
    def 倾角(自己, 倾角 = None):
        return 自己.tiltangle(倾角)
    def 倾斜(自己, 角度):
        自己.tilt(角度)
    def 变形(自己, t11 = None, t12 = None, t21 = None, t22 = None):
        return 自己.shapetransform(t11, t12, t21, t22)
    def 获取形状多边形(自己):
        return 自己.get_shapepoly()
    def 当点击鼠标(自己, 函数, 鼠标键 = 1, 增加 = None):
        自己.onclick(函数, 鼠标键, 增加)
    def 当释放鼠标(自己, 函数, 鼠标键 = 1, 增加 = None):
        自己.onrelease(函数, 鼠标键, 增加)
    def 当拖动鼠标(自己, 函数, 鼠标键 = 1, 增加 = None):
        自己.ondrag(函数, 鼠标键, 增加)
    def 开始记录多边形(自己):
        自己.begin_poly()
    def 结束记录多边形(自己):
        自己.end_poly()
    def 获取多边形(自己):
        return 自己.get_poly()
    def 克隆(自己):        # 调用父类方法, 原问题已解决
        return Turtle.clone(自己)
    def 获取海龟(自己):
        return 自己.getturtle()
    def 获取屏幕(自己):
        return 自己.getscreen()
    def 设置撤消缓冲区(自己, 大小):
        自己.setundobuffer(大小)
    def 撤消缓冲区条目数(自己):
        return 自己.undobufferentries()
    

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
是否在填充 = filling
开始填充 = begin_fill
结束填充 = end_fill
#   更多绘图控制
重置 = reset
清None = clear
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
