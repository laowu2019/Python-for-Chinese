from 内置函数汉化 import *
from 内置类方法汉化 import *

import gc


def set_class_dict(klass, key, value):
    import gc
    d = gc.get_referents(klass.__dict__)[0]
    d[key] = value

set_class_dict(str, "toint", lambda self:int(self))
set_class_dict(str, "居中", lambda self:str.center(self)

#print("123".toint())
print('<' + '你好'.居中(30) + '>')