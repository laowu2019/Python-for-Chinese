关键词字典 = {'假':'False', '空':'None', '真':'True', '且':'and', '或':'or', '是':'is', '非':'not', \
    '定义':'def', '返回':'return', '类':'class', '从':'from', '导入':'import', '以':'with', '为':'as', \
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