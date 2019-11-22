
class A:
    def __init__(self):
        pass

    def __a(self):
        print('_a')

class B(A):

    def _a(self):
        self.__a()
        print('_a')


# B()._a()
import math
# x1, y1 = x-x0, y-y0
# x2, y2 = x-x0, y-y0
x1, y1 = 0.5, 0.75
x2, y2 = -0.5, 1.25
c = math.sqrt((3-2*math.sqrt(2))/6)
d = math.sqrt((3+2*math.sqrt(2))/6)

h, i, j, k = (c*x1-d*y1)**2, (d*x1+c*y1)**2, (c*x2-d*y2)**2, (d*x2+c*y2)**2
n = (j/h-1)/(j/h*i-k)
m = (1-n*k)/j
a, b = math.sqrt(1/m), math.sqrt(1/n)
print(m)
print(n)
# e, f
rag1 = range(1, int(math.pi*10/2), 1)
for r in rag1:
    e = math.cos(r/10)
    f = math.sin(r/10)
    x, y = a*c*e+b*d*f, b*f*(1+d**2)/c-a*d*e
    print((x, y))



# http://baijiahao.com/s?id=1586020045412885527&wfr=spider&for=pc
# https://ruwix.com/the-rubiks-cube/how-to-solve-the-rubiks-cube-beginners-method/
# 魔方小站 http://www.rubik.com.cn/notation.htm

# 1.还需要U2,D2,F2,...(已改进)
# 2.角块颜色(已改进)
# 3.后需增加对ins_str中数字的判断 raise Exception('turn_count Error')(已改进)在主类检查
# 4.写棱块 (已改进)
# 5.写中心块 (已改进)
# 6.写主类，先实例化一个魔方类(已改进)
# 7.动画
# 8.静态时对应色（当前） 接收魔方原始对象，原始坐标对应颜色映射表，通过原始坐标索引颜色，堆小方块顺序函数输出包含颜色
# 9.
