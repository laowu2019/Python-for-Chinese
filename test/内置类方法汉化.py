# 内置类方法汉化
# 下面的一种实现来源于 https://gist.github.com/ruoyu0088/d385f3ca04583c481538751f50adc364, 但不知道如何传递参数
""" 
import gc
import re

def set_class_dict(klass, key, value):
    import gc
    d = gc.get_referents(klass.__dict__)[0]
    d[key] = value

set_class_dict(str, "toint", lambda self:int(self))
set_class_dict(str, "居中", lambda self:str.center(self, 30)

#print("123".toint())
print('<' + '你好'.居中() + '>') """

from 内置函数汉化 import *
from 常量汉化 import *

def 格式化(字符串, *args, **kwargs): # 内置函数已有此功能，不需要？
    return 字符串.format(*args, **kwargs)

def 居中(字符串, 宽度, 填充字符 = ' '):
    return 字符串.center(宽度, 填充字符)

def 查找(字符串, 备查字符串, 开始位置 = 0, 结束位置 = -1):
    return 备查字符串.find(字符串, 开始位置, 结束位置)

def 连接(连接符, 列表):
    return 连接符.join(列表)

def 分割(目标字符串, 分隔符 = 空, 最大数量 = -1):
    return 目标字符串.split(分隔符, 最大数量)

def 小写(字符串):
    return 字符串.lower()

def 大写(字符串):
    return 字符串.upper()    

def 替换(字符串, 原字符串, 新字符串, 替换次数 = -1):
    return 字符串.replace(原字符串, 新字符串, 替换次数)

def 去空格(字符串, 去掉字符 = 空):
    字符串.strip(去掉字符)

def 列表追加(列表, 追加对象):
    列表.append(追加对象)

def 列表清空(列表):
    列表.clear()

def 列表复制(列表):
    return 列表.copy()

def 列表统计(列表, 对象):
    return 列表.count(对象)

def 列表扩展(列表, 扩展列表):
    列表.extend(扩展列表)

def 列表索引(列表, 对象, 开始位置 = 0, 结束位置 = -1):
    return 列表.index(对象, 开始位置, 结束位置)

def 列表插入(列表, 插入位置, 插入对象):
    列表.insert(插入位置, 插入对象)

def 列表弹出(列表, 弹出位置 = -1):
    return 列表.pop(弹出位置)

def 列表移除(列表, 删除对象):
    列表.remove(删除对象)

def 列表反转(列表):
    列表.reverse()

def 列表排序(列表):
    列表.sort()

def 字典清空(字典):
    字典.clear()

def 字典拷贝(字典):
    return 字典.copy()

# 深层拷贝须使用 copy 模块中的 deepcopy 函数

def 字典从键创建(键表, 值 = 空, 字典 = {}):
    return 字典.fromkeys(键表, 值)    

def 字典取值(字典, 键, 不存在时返回值 = 空):
    return 字典.get(键, 不存在时返回值)

def 字典项(字典):
    return 字典.items()

def 字典键(字典):
    return 字典.keys()

def 字典弹出(字典, 键, 不存在时返回值 = 空):
    return 字典.pop(键, 不存在时返回值)

def 字典弹出末项(字典):
    return 字典.popitem()

def 字典设置默认值(字典, 键, 默认值 = 空):
    return 字典.setdefault(键, 默认值)

def 字典更新(字典, 新字典):
    字典.update(新字典)

def 字典值(字典):
    return 字典.values()



