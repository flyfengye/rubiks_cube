default = [['ABE', 'BE', 'BCE', 'CE', 'CDE', 'DE', 'DAE', 'AE', 'E'],
           ['AB', 'B', 'BC', 'C', 'CD', 'D', 'DA', 'A', ''],
           ['ABF', 'BF', 'BCF', 'CF', 'CDF', 'DF', 'DAF', 'AF', 'F']]


class CornerPieces:
    def __init__(self):
        self.position_default = (1, 1, 1)
        self.position = (1, 1, 1)

        self.pose_default = ('u', 'f', 'r')
        self.pose = ('u', 'f', 'r')

    def turn(self, ins_str):
        x, y, z = self.position
        xy, xz, yz = self.pose

        if 'U' in ins_str or 'D' in ins_str:
            if (ins_str == "U" and z == 1) or (ins_str == "D'" and z == -1):
                x, y = self._planar_pos((x, y))
                xz, yz = yz, xz
            elif (ins_str == "U'" and z == 1) or (ins_str == "D" and z == -1):
                x, y = self._planar_pos((x, y), clockwise=False)
                xz, yz = yz, xz
            elif ins_str in ("U2", "U'2", "D2", "D'2") and (z == 1 or z == -1):
                x, y = -x, -y
            else:
                return

        elif 'R' in ins_str or 'L' in ins_str:
            if (ins_str == "R" and x == 1) or (ins_str == "L'" and x == -1):
                y, z = self._planar_pos((y, z))
                xy, xz = xz, xy
            elif (ins_str == "R'" and x == 1) or (ins_str == "L" and x == -1):
                y, z = self._planar_pos((y, z), clockwise=False)
                xy, xz = xz, xy
            elif ins_str in ("R2", "R'2", "L2", "L'2") and (x == 1 or x == -1):
                y, z = -y, -z
            else:
                return

        elif 'F' in ins_str or 'B' in ins_str:
            if (ins_str == "F" and y == -1) or (ins_str == "B'" and y == 1):
                x, z = self._planar_pos((x, z))
                xy, yz = yz, xy
            elif (ins_str == "F'" and y == -1) or (ins_str == "B" and y == 1):
                x, z = self._planar_pos((x, z), clockwise=False)
                xy, yz = yz, xy
            elif ins_str in ("F2", "F'2", "B2", "B'2") and (y == 1 or y == -1):
                x, z = -x, -z
            else:
                return

        else:
            raise Exception('ins_str Error2')

        self.position = (x, y, z)
        self.pose = (xy, xz, yz)

    @staticmethod
    def _planar_pos(pos, turn_count=1, clockwise=True):  # 后需对参数进行删减必要时写成实例变量
        pos_all = ((1, 1), (1, -1), (-1, -1), (-1, 1))
        if clockwise is True:
            return pos_all[(pos_all.index(pos) + turn_count) % 4]
        else:
            return pos_all[(pos_all.index(pos) - turn_count) % 4]


class EdgePieces(CornerPieces):
    @staticmethod
    def _planar_pos(pos, turn_count=1, clockwise=True):  # 后需对参数进行删减必要时写成实例变量
        pos_all = ((1, 0), (0, -1), (-1, 0), (1, 0))
        if clockwise is True:
            return pos_all[(pos_all.index(pos) + turn_count) % 4]
        else:
            return pos_all[(pos_all.index(pos) - turn_count) % 4]


class CenterPieces:
    def __init__(self):
        pass


if __name__ == '__main__':
    crn = EdgePieces()
    crn.position = (1, 0, 1)
    crn.pose = ('u', '', 'r')
    crn.turn("U")
    print(crn.position)
    print(crn.pose)
