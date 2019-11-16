class DrawRubikS:
    def __init__(self, pos_color_tuple):
        # for pos_color in pos_color_tuple:
        #     self.draw(pos_color)
        pass

    def add_all_cube(self):
        cps = self.center_point(1)
        cps = dict(cps)

        src = [(-1, 0, 1), (1, 0, -1)]
        order_26 = []
        for k in src[0]:
            for j in src[1]:
                for i in src[0]:
                    order_26.append((i, j, k))

        order_26.remove((0, 0, 0))
        for p in order_26:
            # print(cps[p])
            yield self.get_cube_face_pos(cps[p])

    def get_cube_face_pos(self, cp):
        # cp: the center point position of cube
        us, ds = self.vertex_pos(cp, 40 // 3 + 6)
        a, b, c, d = us
        e, f, g, h = ds
        six_face = list()  # d, l, b, f, r, u
        six_face.append(ds)
        six_face.append((a, b, f, e))
        six_face.append((d, a, e, h))
        six_face.append((b, c, g, f))
        six_face.append((c, d, h, g))
        six_face.append(us)
        return six_face

    def get_cube_color_pos(self):
        pass

    def center_point(self, pos_color):
        center_pos = (900, 300)
        # pos, color = pos_color
        pos = (1, 1, 1)
        color = ('u', 'b', 'r')
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
    all = dr.add_all_cube()
    for xx in all:
        print(xx)
        exit()
    # f = open('你要读取的txt', 'r', encoding='utf-8')
    # lines = f.readlines()
    # for line in lines:
    #     first_char = line[0]

