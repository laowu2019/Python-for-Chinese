"""Define the menu contents, hotkeys, and event bindings.

There is additional configuration information in the EditorWindow class (and
subclasses): the menus are created there based on the menu_specs (class)
variable, and menus not created are silently skipped in the code here.  This
makes it possible, for example, to define a Debug menu which is only present in
the PythonShell window, and a Format menu which is only present in the Editor
windows.

"""
from importlib.util import find_spec

from idlelib.config import idleConf

#   Warning: menudefs is altered in macosx.overrideRootMenu()
#   after it is determined that an OS X Aqua Tk is in use,
#   which cannot be done until after Tk() is first called.
#   Do not alter the 'file', 'options', or 'help' cascades here
#   without altering overrideRootMenu() as well.
#       TODO: Make this more robust

menudefs = [
 # underscore prefixes character to underscore
 ('file', [
   ('新建文件', '<<open-new-window>>'),
   ('打开', '<<open-window-from-file>>'),
   ('打开模块', '<<open-module>>'),
   ('模块浏览器', '<<open-class-browser>>'),
   ('路径浏览器', '<<open-path-browser>>'),
   None,
   ('保存', '<<save-window>>'),
   ('另存为', '<<save-window-as-file>>'),
   ('副本另存为', '<<save-copy-of-window-as-file>>'),
   None,
   ('打印窗口', '<<print-window>>'),
   None,
   ('关闭', '<<close-window>>'),
   ('退出', '<<close-all-windows>>'),
   ]),

 ('edit', [
   ('撤销', '<<undo>>'),
   ('恢复', '<<redo>>'),
   None,
   ('剪切', '<<cut>>'),
   ('复制', '<<copy>>'),
   ('粘贴', '<<paste>>'),
   ('选择全部', '<<select-all>>'),
   None,
   ('查找', '<<find>>'),
   ('再次查找', '<<find-again>>'),
   ('查找选定内容', '<<find-selection>>'),
   ('文件中查找', '<<find-in-files>>'),
   ('替换', '<<replace>>'),
   ('前往行', '<<goto-line>>'),
   ('显示补全', '<<force-open-completions>>'),
   ('扩展字词', '<<expand-word>>'),
   ('显示调用提示', '<<force-open-calltip>>'),
   ('显示包围括号', '<<flash-paren>>'),
   ]),

 ('format', [
   ('向右缩进区域', '<<indent-region>>'),
   ('向左缩进区域', '<<dedent-region>>'),
   ('注释区域', '<<comment-region>>'),
   ('取消注释区域', '<<uncomment-region>>'),
   ('区域制表符化', '<<tabify-region>>'),
   ('取消区域制表符', '<<untabify-region>>'),
   ('切换制表符', '<<toggle-tabs>>'),
   ('新缩进宽度', '<<change-indentwidth>>'),
   ('格式化段落', '<<format-paragraph>>'),
   ('去除尾随空格', '<<do-rstrip>>'),
   ]),

 ('run', [
   ('草蟒 Shell', '<<open-python-shell>>'),
   ('检查模块', '<<check-module>>'),
   ('运行模块', '<<run-module>>'),
   ]),

 ('shell', [
   ('查看上次重启', '<<view-restart>>'),
   ('重启 Shell', '<<restart-shell>>'),
   None,
   ('前一历史记录', '<<history-previous>>'),
   ('下一历史记录', '<<history-next>>'),
   None,
   ('中断执行', '<<interrupt-execution>>'),
   ]),

 ('debug', [
   ('前往文件/行', '<<goto-file-line>>'),
   ('!调试器', '<<toggle-debugger>>'),
   ('堆栈查看器', '<<open-stack-viewer>>'),
   ('!自动打开堆栈查看器', '<<toggle-jit-stack-viewer>>'),
   ]),

 ('options', [
   ('配置 _IDLE', '<<open-config-dialog>>'),
   None,
   ('显示代码上下文 _Code Context', '<<toggle-code-context>>'),
   ('缩放高度', '<<zoom-height>>'),
   ]),

 ('window', [
   ]),

 ('help', [
   ('关于 IDLE', '<<about-idle>>'),
   None,
   ('_IDLE 帮助', '<<help>>'),
   ('草蟒文档', '<<python-docs>>'),
   ]),
]

if find_spec('turtledemo'):
    menudefs[-1][1].append(('海龟演示', '<<open-turtle-demo>>'))

default_keydefs = idleConf.GetCurrentKeySet()

if __name__ == '__main__':
    from unittest import main
    main('idlelib.idle_test.test_mainmenu', verbosity=2)
