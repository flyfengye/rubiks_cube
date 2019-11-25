from check_tuple import UD
from check_tuple import RL
from check_tuple import FB


class CornerPieces:
    pos_order = ((1, 1), (1, -1), (-1, -1), (-1, 1))

    def __init__(self, position_default, color_default):
        self.position_default = position_default
        self.position = position_default

        self.color_default = color_default
        self.color = color_default

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

        # for m, n in judge_tb['turn_twice']:
        #     if ins_str == m and third_pos == n:
        #         _one, _two = planar_pos
        #         return (-_one, -_two), two_color

    def turn(self, ins_str):
        self.ins_str = ins_str
        ins_strip = ins_str.strip("2'")  # 转动两次情况在主类进行拆分

        x, y, z = self.position
        xy, xz, yz = self.color

        if ins_strip in ('U', 'D', 'E', 'u', 'd', 'y'):  # 这里是否每次新建元组拖cpu
            if (x, y) != (0, 0):  # 中心块pos不改变
                res = self.__judge(UD, (x, y), z, (xz, yz))
                if res:
                    x, y = res[0]
                    xz, yz = res[1]

        elif ins_strip in ('R', 'L', 'M', 'r', 'l', 'x'):
            if (y, z) != (0, 0):
                res = self.__judge(RL, (y, z), x, (xy, xz))
                if res:
                    y, z = res[0]
                    xy, xz = res[1]

        elif ins_strip in ('B', 'F', 'S', 'b', 'f', 'z'):
            if (x, z) != (0, 0):
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
        # print(self.__class__)#debug
        # print(pos_order)
        # print(pos)
        # print(self.position)
        if clockwise is True:
            return pos_order[(pos_order.index(pos) + turn_count) % 4]
        else:
            return pos_order[(pos_order.index(pos) - turn_count) % 4]


class EdgePieces(CornerPieces):
    pos_order = ((1, 0), (0, -1), (-1, 0), (0, 1))


class CenterPieces(EdgePieces):
    pass


class RubikS:
    def __init__(self):
        self.all_pieces = self.__init_all_pieces()
        self.ins_str = ''
        self.ins_axis = ''

    @staticmethod
    def __init_all_pieces():
        u, d, f, b, r, _l = (0, 'u', 1), (0, 'd', -1), (1, 'f', -1), (1, 'b', 1), (2, 'r', 1), (2, 'l', -1)

        cor_grp = ((u, d), ((b, f), (r, _l)))
        edg_grp1 = ((u, d), (b, f, r, _l))
        edg_grp2 = ((b, f), (r, _l))
        cet_grp = (u, d, b, f, r, _l)
        cor_grp = tuple((i, m, n) for n in cor_grp[1][1] for m in cor_grp[1][0] for i in cor_grp[0])
        edg_grp = tuple((i, j) for j in edg_grp1[1] for i in edg_grp1[0]) + \
            tuple((i, j) for j in edg_grp2[1] for i in edg_grp2[0])

        def get_pc(dft, index, *args):
            _pc = [dft] * 3
            for arg in args:
                _pc[arg[0]] = arg[index]
            if dft == 0:
                _pc.reverse()
            return tuple(_pc)
        cor_pis = tuple(CornerPieces(get_pc(0, 2, i, m, n), get_pc('', 1, i, m, n)) for i, m, n in cor_grp)
        edg_pis = tuple(EdgePieces(get_pc(0, 2, i, j), get_pc('', 1, i, j)) for i, j in edg_grp)
        cet_pis = tuple(CenterPieces(get_pc(0, 2, i), get_pc('', 1, i)) for i in cet_grp)

        return cor_pis + edg_pis + cet_pis

    def turn(self, ins_str):
        self.ins_str = self.__check_ins_str(ins_str) # 下面再加判断是否含有2有则拆分，U2 U-U
        for _pieces in self.all_pieces:
            _pieces.turn(self.ins_str)

    @staticmethod
    def __check_ins_str(ins_str):
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
        return ins_str


if __name__ == '__main__':
    # crn = CenterPieces((0, 0, 1), ('u', '', ''))
    # crn = CenterPieces((0, 1, 0), ('', 'd', ''))
    # crn.turn("D'")
    # print(crn.position)
    # print(crn.color)

    rbk = RubikS()
    a_p1 = set()
    count = 1
    for pieces in rbk.all_pieces:
        print(f"pieces: {count}")
        a_p1.add(pieces.position)
        print(pieces.position)
        print(pieces.color)
        count += 1
    print('-' * 20)

    count = 1
    equation_str = "R'-U'-R-U'-R'-U'-U'-R-U'-"
    equation_str += "L-U-L'-U-L-U'-U'-L'-U-"
    equation_str += "L-U-L'-U-L-U'-U'-L'-U-"
    equation_str += "R'-U'-R-U'-R'-U'-U'-R-U'"
    all_ins = equation_str.split('-')
    for ins_ in all_ins:
        rbk.turn(ins_)
    a_p = set()
    for pieces in rbk.all_pieces:
        print(f"pieces: {count}")
        a_p.add(pieces.position)
        print(pieces.position)
        print(pieces.color)
        count += 1
    print(a_p)
    print(a_p1)
    if a_p == a_p1:
        print('yes')
    print(len(a_p))