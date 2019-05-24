# 运行中文程序的入口
# coding='UTF-8'

from 汉化包 import * 
import sys
#import os

#try:
#os.chdir(os.path.dirname(__file__))
#print(os.getcwd())
exec(代码回译(sys.argv[1]))
#exec(代码回译('示例1.py'))
#except:
#    print('没有输入或找到要运行的文件。')
