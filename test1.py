from check_tuple import UD
from check_tuple import RL
from check_tuple import FB

default = [['ABE', 'BE', 'BCE', 'CE', 'CDE', 'DE', 'DAE', 'AE', 'E'],
           ['AB', 'B', 'BC', 'C', 'CD', 'D', 'DA', 'A', ''],
           ['ABF', 'BF', 'BCF', 'CF', 'CDF', 'DF', 'DAF', 'AF', 'F']]


class CornerPieces:
    pos_order = ((1, 1), (1, -1), (-1, -1), (-1, 1))

    def __init__(self):
        self.position_default = (1, 1, 1)
        self.position = (1, 1, 1)

        self.color_default = ('u', 'f', 'r')
        self.color = ('u', 'f', 'r')

        self.ins_str = ''

    def __judge(self, judge_tb, planar_pos, third_pos, two_color):
        ins_str = self.ins_str
        for m, n in judge_tb['clockwise']:
            if ins_str == m and third_pos == n:
                one, two = two_color
                return self.__planar_pos(planar_pos), (two, one)

        for m, n in judge_tb['anticlockwise']:
            if ins_str == m and third_pos == n:
                one, two = two_color
                return self.__planar_pos(planar_pos, clockwise=False), (two, one)

        for m, n in judge_tb['turn_twice']:
            if ins_str == m and third_pos == n:
                _one, _two = planar_pos
                return (-_one, -_two), two_color

    def turn(self, ins_str):
        self.ins_str = ins_str
        ins_strip = ins_str.strip("2'")

        x, y, z = self.position
        xy, xz, yz = self.color

        if ins_strip in ('U', 'D', 'E', 'u', 'd', 'y'):
            res = self.__judge(UD, (x, y), z, (xz, yz))
            if res:
                x, y = res[0]
                xz, yz = res[1]

        elif ins_strip in ('R', 'L', 'M', 'r', 'l', 'x'):
            res = self.__judge(RL, (y, z), x, (xy, xz))
            if res:
                y, z = res[0]
                xy, xz = res[1]

        elif ins_strip in ('B', 'F', 'S', 'b', 'f', 'z'):
            res = self.__judge(FB, (x, z), y, (xy, yz))
            if res:
                x, z = res[0]
                xy, yz = res[1]

        else:
            raise Exception('ins_str Error')  # 若检查了ins_str则不会报错

        self.position = (x, y, z)
        self.color = (xy, xz, yz)

    def __planar_pos(self, pos, turn_count=1, clockwise=True):  # 后需对参数进行删减必要时写成实例变量
        pos_order = self.pos_order
        if clockwise is True:
            return pos_order[(pos_order.index(pos) + turn_count) % 4]
        else:
            return pos_order[(pos_order.index(pos) - turn_count) % 4]

    def __check_ins_str(self, ins_str):  # 后面在主类检查
        """指定字母、单引号、数字2，最多各1个"""
        ins_str = ins_str.strip()
        if len(ins_str) > 3:
            raise Exception('ins_str length > 3')

        ins_all = ('U', 'D', 'E', 'u', 'd', 'y', 'R', 'L', 'M', 'r', 'l', 'x', 'B', 'F', 'S', 'b', 'f', 'z')

        if len([i for i in ins_all if i in ins_str]) > 1:
            raise Exception('ins_str 字母 > 1')

        if ins_str.count("'") > 1:
            raise Exception('ins_str 单引号 > 1')

        if ins_str.count("2") > 1:
            raise Exception('ins_str 数字2 > 1')

        for ins_s in ins_str:
            if ins_s not in ins_all and ins_s not in ("'", '2'):
                raise Exception('ins_str 含有其它字符')
        self.ins_str = ins_str


class EdgePieces(CornerPieces):
    pos_order = ((1, 0), (0, -1), (-1, 0), (0, 1))


class CenterPieces(EdgePieces):
    pass


if __name__ == '__main__':
    crn = CenterPieces()
    crn.position = (0, 0, 1)
    crn.color = ('r', '', '')
    crn.turn("M'")
    print(crn.position)
    print(crn.color)
