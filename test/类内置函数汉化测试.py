""" __初始化__ = classmethod(class.__init__())
显示 = print
class 空类:
    def __初始化__(实例):
        显示('我是一个类，来自比特世界。')

空空 = 空类() 
类的汉化：定义一个太极类作为基类，"""
""" def __init__(*参数):
    pass
__初始化__ = __init__ """

class 太极:
    def __init__(实例):
        实例.__初始化__()
    def __初始化__(实例):
        print('我是太极')
    def __call__(实例):
        实例.__调用__()
    def __调用__(实例):
        print('调用太极')

class 两仪(太极):
    def __初始化__(实例):
        print('我是两仪')
    def __调用__(实例):
        print('调用两仪')

class 四象(两仪):
    pass

八卦 = 四象()
八卦()


