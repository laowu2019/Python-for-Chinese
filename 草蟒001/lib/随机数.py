from random import *

# 随机数(), 0 - 1, 含 0 不含 1
随机数 = random

# 随机整数(m, n), m - n 之间的整数, 含 m 和 n
随机整数 = randint

# 随机浮点数(a, b), a - b 之间的浮点数, 含 a 和 b, a 和 b 可以是浮点数
随机浮点数 = uniform

# 随机范围数(m, n, 步长), 在一个递增整数序列中随机选择一个整数
随机范围数 = randrange

# 随机单选(序列), 随机多选(序列, k)返回一个列表
随机单选 = choice
随机多选 = sample

# 随机打乱(序列), 返回空, 直接修改原序列
随机打乱 = shuffle

