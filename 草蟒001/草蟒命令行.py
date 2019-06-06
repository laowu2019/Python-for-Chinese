import code
import 汉化包

class 草蟒解释器(code.InteractiveInterpreter):
    def runsource(self, source, filename="<input>", symbol="single"):
        source = 汉化包.替换中文名称(source, 0)
        try:
            code = self.compile(source, filename, symbol)
        except (OverflowError, SyntaxError, ValueError):
            # Case 1
            self.showsyntaxerror(filename)
            return False

        if code is None:
            # Case 2
            return True

        # Case 3
        self.runcode(code)
        return False

class 草蟒控制台(code.InteractiveConsole,草蟒解释器):
    pass

控制台 = 草蟒控制台()
控制台.interact('草蟒命令行 3.7.3\n')