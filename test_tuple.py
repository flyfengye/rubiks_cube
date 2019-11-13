print((*(1, 2), 3))
class A:
    def __init__(self):
        pass

    def __a(self):
        print('_a')

class B(A):

    def _a(self):
        self.__a()
        print('_a')

B()._a()
# http://baijiahao.com/s?id=1586020045412885527&wfr=spider&for=pc
# https://ruwix.com/the-rubiks-cube/how-to-solve-the-rubiks-cube-beginners-method/
# 魔方小站 http://www.rubik.com.cn/notation.htm

# 1.还需要U2,D2,F2,...(已改进)
# 2.角块颜色(已改进)
# 3.后需增加对ins_str中数字的判断 raise Exception('turn_count Error')(已改进)在主类检查
# 4.写棱块 (已改进)
# 5.写中心块 (已改进)
# 6.写主类，先实例化一个魔方类(已改进)
# 7.动画(当前)
