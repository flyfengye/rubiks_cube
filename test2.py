from check_tuple import UD, RL, FB
from test1 import CornerPieces
from test1 import EdgePieces
from test1 import CenterPieces


class DrawRubikS:
    def __init__(self, rubik_obj):
        self.rubik_obj = rubik_obj
        self.all_pieces = rubik_obj.all_pieces  # 若只有单函数使用则移至该函数
        self.old_pcs = []

    def get_cec(self):
        ins_str = self.rubik_obj.ins_str.strip("'")
        if ins_str in ('U', 'D', 'E', 'u', 'd', 'y'):
            pos_md = (2, 1)
        elif ins_str in ('R', 'L', 'M', 'r', 'l', 'x'):
            pos_md = (0, 1)
        elif ins_str in ('B', 'F', 'S', 'b', 'f', 'z'):
            pos_md = (1, 1)
        else:
            raise Exception('ins_str error')
        return pos_md


    def add_all_action(self):
        # 转动层所有块的坐标改变
        # 获取起点对应终点坐标，计算轨迹
        # 先绘制一个角块尝试
        idx = 0
        tmp_corner_pcs = []
        tmp_edge_pcs = []
        tmp_center_pc = ()
        ct_pos = ''
        for new_pc in self.add_all_cube():
            old_pc = self.old_pcs[idx]
            if new_pc != old_pc:  # 字典索引速度和列表idx索引速度那个快？
                if 0 not in old_pc[2]:
                    tmp_corner_pcs.append(old_pc)
                elif old_pc[2].count(0) == 1:
                    tmp_edge_pcs.append(old_pc)
            if ()
        tmp_center_pc = old_pc
        cn_order = CornerPieces.pos_order
        eg_order = EdgePieces.pos_order
        ct_order = CenterPieces.pos_order
        for corner_pc in tmp_corner_pcs




        # xxx
        #
        # (e, f, g, h) 1
        # (a, b, f, e) 2
        # (d, a, e, h) 3
        # (b, c, g, f) 4
        # (c, d, h, g) 5
        # (a, b, c, d) 6
        #
        #
        # (a, b, c, d)
        # (e, f, g, h)
        #
        # (a, b, c, d)
        # (e, a, b, h)
        #
        # a,b  e,f
        # c,d  g,h

        (_a, _b, _c, _d) = (1, 2, 3, 4)
        (_e, _f, _g, _h) = (5, 6, 7, 8)
        (a, b, c, d) = (_e, _f, _a, _b)
        (e, f, g, h) = ()
        # 先堆不动块，
        # 直接动块进行轨迹生产,动块要判断堆放顺序
        # 动块终点坐标对应出来，根据turn判定，（当前）
        # 计算椭圆轨迹角度，生成新坐标
        # 最好在循环中就把动作pcs添加起来
        # 动画时颜色还是按照old添，但是到了一定角度，需改变堆放pos和color的顺序
    def vertex_reorder(self, old_pc_0):
        ins_str_0 = self.rubik_obj.ins_str
        ins_str = ins_str_0.strip("'")

        (a, b, c, d) = old_pc_0[-1]
        (e, f, g, h) = old_pc_0[0]

        if ins_str in ('U', 'D', 'E', 'u', 'd', 'y'):
            if any(m if m == ins_str_0 else '' for m, _ in UD['clockwise']):
                us = (b, c, d, a)  # 是否有快速移位的方法
                ds = (f, g, h, e)
            else:
                us = (d, a, b, c)
                ds = (h, e, f, g)

        elif ins_str in ('R', 'L', 'M', 'r', 'l', 'x'):
            if any(m if m == ins_str_0 else '' for m, _ in RL['clockwise']):
                us = (b, f, g, c)
                ds = (a, e, h, d)
            else:
                us = (e, a, d, h)
                ds = (f, b, c, g)

        elif ins_str in ('B', 'F', 'S', 'b', 'f', 'z'):
            if any(m if m == ins_str_0 else '' for m, _ in FB['clockwise']):
                us = (e, f, b, a)
                ds = (h, g, c, d)
            else:
                us = (d, c, g, h)
                ds = (a, b, f, e)
        else:
            raise Exception('ins_str error')

        return self.get_six_fp(us, ds)

    def bak_pcs(self):
        self.old_pcs = self.new_pcs.copy()

    def add_all_cube(self):

        cps = self.center_point()
        cps = dict(cps)

        cs = {cube.position: cube.color for cube in self.all_pieces}
        # position:color of all

        src = [(-1, 0, 1), (1, 0, -1)]
        order_26 = []
        for k in src[0]:
            for j in src[1]:
                for i in src[0]:
                    order_26.append((i, j, k))

        order_26.remove((0, 0, 0))
        for p in order_26:
            # print(cps[p])
            pc = self.get_cube_face_pos(cps[p]), self.get_cube_face_color(p, cs[p]), p
            print(pc)
            yield pc

    @staticmethod
    def get_cube_face_color(pos, color):
        x, y, z = pos
        xy, xz, yz = color
        six_fc = [''] * 6  # d, l, b, f, r, u

        idx = 0
        for i, j in ((z, xy), (x, yz), (y, xz)):
            if i == 1:
                six_fc[-idx-1] = j
            elif i == -1:
                six_fc[idx] = j
            idx += 1
        six_fc[2], six_fc[3] = six_fc[3], six_fc[2]

        return six_fc  # six face color

    def get_cube_face_pos(self, cp):
        # cp: the center point position of cube
        us, ds = self.vertex_pos(cp, 40 // 3 + 6)
        return self.get_six_fp(us, ds)

    @staticmethod
    def get_six_fp(us, ds):
        a, b, c, d = us
        e, f, g, h = ds
        six_fp = list()  # d, l, b, f, r, u
        six_fp.append(ds)
        six_fp.append((a, b, f, e))
        six_fp.append((d, a, e, h))
        six_fp.append((b, c, g, f))
        six_fp.append((c, d, h, g))
        six_fp.append(us)
        return six_fp  # six face position

    def center_point(self):
        center_pos = (900, 300)
        # [(600, 200), (450, 150), (600, 100), (750, 150)],
        # [(600, 200), (450, 150), (450, 350), (600, 400)],
        # [(600, 200), (750, 150), (750, 350), (600, 400)],
        #
        # [(600, 195), (465, 150), (600, 105), (735, 150)]
        # [(592.5, 210), (457.5, 162.5), (457.5, 342.5), (592.5, 390)]
        # [(607.5, 210), (742.5, 162.5), (742.5, 342.5), (607.5, 390)]

        us, ds = self.vertex_pos(center_pos, t=40)
        cps = set()  # cps: the center point position of all cube
        pos_order1 = ((-1, 1), (-1, -1), (1, -1), (1, 1))
        pos_order2 = ((-1, 0), (0, -1), (1, 0), (0, 1))
        four_pos = []  # four_pos: the midpoint of the four pillars
        cps.add(((0, 0, 1), self.mid_pos(us[1], us[3])))
        cps.add(((0, 0, -1), self.mid_pos(ds[1], ds[3])))

        for i in range(0, 4):
            cps.add((pos_order1[i] + (1,), us[i]))
            cps.add((pos_order1[i] + (-1,), ds[i]))
            tmp_pos = self.mid_pos(us[i], ds[i])
            four_pos.append(tmp_pos)
            cps.add((pos_order1[i] + (0,), tmp_pos))
            cps.add((pos_order2[i] + (1,), self.mid_pos(us[i], us[(i + 1) % 4])))
            cps.add((pos_order2[i] + (-1,), self.mid_pos(ds[i], ds[(i + 1) % 4])))

        for i in range(0, 4):
            cps.add((pos_order2[i] + (0,), self.mid_pos(four_pos[i], four_pos[(i + 1) % 4])))

        return cps
        # for c in cps:
        #     _us, _ds = self.vertex_pos(c[1], t=40 // 3 - 2)
        #     print(_us)
        #     print(_ds)
        #     exit()

    @staticmethod
    def vertex_pos(center_pos, t):
        x, y = center_pos
        t2, t3 = t * 2, t * 3
        us = ((x, y - t3), (x - t3, y - t2), (x, y - t), (x + t3, y - t2))
        ds = ((x, y + t), (x - t3, y + t2), (x, y + t3), (x + t3, y + t2))
        return us, ds

    @staticmethod
    def mid_pos(p1, p2):
        return (p1[0] + p2[0]) // 2, (p1[1] + p2[1]) // 2  # 1.70  2.16


if __name__ == '__main__':
    dr = DrawRubikS(1)
    all = dr.get_cube_face_color(1, 1)
    for xx in all:
        print(xx)
        # exit()
    # f = open('你要读取的txt', 'r', encoding='utf-8')
    # lines = f.readlines()
    # for line in lines:
    #     first_char = line[0]

