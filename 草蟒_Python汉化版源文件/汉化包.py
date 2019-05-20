import os

关键词字典 = {'假':'False', '空':'None', '真':'True', '且':'and', '或':'or', '是':'is', '非':'not', \
    '定义':'def', '返回':'return', '类':'class', '从':'from', '导入':'import', '用':'with', '为':'as', \
        '取':'for', '在':'in', '如果':'if', '不然':'elif', '否则':'else', '只要':'while', '过':'continue', \
            '跳出':'break', '尝试':'try', '捕获':'except', '示警':'raise', '最后':'finally', '断言':'assert', \
                '删除':'del', '全局':'global', '非局部':'nonlocal', '雷锋':'lambda', '无操作':'pass', \
                    '产生':'yield', '异步':'async', '等待':'await', '不在':'not in', '不是':'is not'}

内置函数字典 = {'显示':'print', '输入':'input', '求值':'eval', '绝对值':'abs', '最大值':'max', '最小值':'min', \
    '求和':'sum', '指数':'pow', '商和余数':'divmod', '舍入':'round', '复数':'complex', '布尔':'bool', '整数':'int', \
    '字符串':'str', '浮点数':'float', '元组':'tuple', '列表':'list', '字典':'dict', '集合':'set', '长度':'len', \
    '二进制':'bin', '八进制':'oct', '十六进制':'hex', '字符':'chr', 'U编码':'ord', '返回ASCII':'ascii', \
    '字节数组':'bytearray', '字节':'bytes', '枚举':'enumerate', '格式化':'format', '范围':'range', '映射':'map', \
    '全部为真':'all', '任一为真':'any', '反转':'reversed', '排序':'sorted', '打开':'open', '执行':'exec', \
    '编译':'compile', '断点':'breakpoint', '是否可调用':'callable', '删除属性':'delattr', '获取属性':'getattr', \
    '设置属性':'setattr', '是否存在属性':'hasattr', '名称列表':'dir', '帮助':'help', '过滤器':'filter', \
    '迭代对象':'iter', '下一个':'next', '哈希值':'hash', '标识':'id', '是否实例':'isinstance', '是否子类':'issubclass', \
    '对象':'object', '静态方法':'staticmethod', '类方法':'classmethod', '内存视图':'memoryview', '类型':'type', \
    '切片':'slice', '超类':'super', '属性':'property', '冻结集合':'frozenset', '对象字典属性':'vars', \
    '局部符号字典':'locals', '全局符号字典':'globals', '可打印字符串':'repr', '迭代器':'zip', '__导入__':'__import__', \
    '退出':'exit'}

名称字典大全 = dict(关键词字典, **内置函数字典)

中文关键词 = list(关键词字典.keys())

中文内置函数名 = list(内置函数字典.keys())

中文名称大全 = 中文关键词 + 中文内置函数名

def 替换中文名称(source, script = 1): # script: 脚本需解码, 命令行输入不解码.
    import tokenize, token
    from io import StringIO

    tokenlist = []
    if script:
        source = source.decode('UTF-8')
    t = tokenize.generate_tokens(StringIO(source).readline)    
    for tokentype, tokenstring, tokenbegin, tokenend, tokenline in t:
        if tokentype == token.NAME and tokenstring in 中文名称大全: 
            tokenlist.append((tokentype, 名称字典大全.get(tokenstring), tokenbegin, tokenend, tokenline))
        else:
            tokenlist.append((tokentype, tokenstring, tokenbegin, tokenend, tokenline))
    return tokenize.untokenize(tokenlist)

def 查找匹配英文文件(资源名, 资源绝对路径, 资源所在目录):
    import glob

    英文文件名 = 资源名[:-3] + '_英.py'
    草蟒缓存路径 = 资源所在目录 +'\\__草蟒缓存__'
    英文名绝对路径 = 草蟒缓存路径 + '\\' + 英文文件名
    if not os.path.exists(草蟒缓存路径):
        os.makedirs(草蟒缓存路径)
        fp = open(草蟒缓存路径 + "\\__init__.py", 'w')
        fp.close()
    #print(glob.glob(草蟒缓存路径 + '\\*'))
    if 英文名绝对路径 in glob.glob(草蟒缓存路径 + '\\*'):
        中文文件状态 = os.stat(资源绝对路径)
        #print(中文文件状态.st_mtime)
        英文文件状态 = os.stat(英文名绝对路径)
        #print(英文文件状态.st_mtime)
        if 英文文件状态.st_mtime >= 中文文件状态.st_mtime:
            return True
    else:
        return False

def 导入中文资源(资源名, 资源所在目录 = None):
    # .py 形式的资源名 (例如 '某种资源.py') 为必填参数, 资源所在目录为选填参数.
    import importlib
    import sys

    #print(os.getcwd())
    if 资源所在目录 is None:
        资源绝对路径 = os.path.abspath(资源名)
        资源所在目录 = os.path.dirname(资源绝对路径)
    else:
        资源绝对路径 = 资源所在目录 + '\\' + 资源名
    #sys.path.append(资源所在目录)
    if not 查找匹配英文文件(资源名, 资源绝对路径, 资源所在目录):
        with open(资源绝对路径, 'rb') as f:
            s = f.read()
            source = 替换中文名称(s)
        with open(资源所在目录 + '\\__草蟒缓存__\\' + 资源名[:-3] + '_英.py', 'w', encoding='UTF-8') as fe:
            fe.write(source)
    #os.chdir('__草蟒缓存__')
    #print(os.getcwd())
    return importlib.import_module('__草蟒缓存__.' + 资源名[:-3] + '_英')
    # 以上方法尚未完全掌握, 下面是 Python 文档中提供的文件导入方法
    # import tokenize
    #file_path = tokenize.__file__
    #module_name = tokenize.__name__
    #spec = importlib.util.spec_from_file_location(资源名[:-3] + '_英.py', 资源所在目录 + '\\__草蟒缓存__\\')
    #module = importlib.util.module_from_spec(spec)
    #return spec.loader.exec_module(module)
    #以上方法似乎更困难.


def 代码回译(文件名):
    with open(文件名, 'rb') as f:
        源代码 = f.read()
    return 替换中文名称(源代码)

def 文件回译(文件名):
    with open(文件名, 'rb') as f:
        中文文件 = f.read()
        英文文件 = 替换中文名称(中文文件)
    with open(文件名[:-3] + '_英.py', 'w', encoding='UTF-8') as fe:
        fe.write(英文文件)    