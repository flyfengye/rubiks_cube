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
# 1.还需要U2,D2,F2,...
# 2.角块姿势(当前)