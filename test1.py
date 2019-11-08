default = [['ABE', 'BE', 'BCE', 'CE', 'CDE', 'DE', 'DAE', 'AE', 'E'],
           ['AB', 'B', 'BC', 'C', 'CD', 'D', 'DA', 'A', ''],
           ['ABF', 'BF', 'BCF', 'CF', 'CDF', 'DF', 'DAF', 'AF', 'F']]


class CornerPieces:
    def __init__(self):
        self.position = (1, 1, 1)

    def turn(self, ins_str):
        if ins_str == 'U':
            x, y, z = self.position
            if z == 1:
                self.position = self.__clockwise((x, y)) + z

    @staticmethod
    def __clockwise(_pos):
        df = ((1, 1), (1, -1), (-1, -1), (-1, 1))
        return df[(df.index(_pos) + 1) % 4]


class EdgePieces:
    def __init__(self):
        pass


class CenterPieces:
    def __init__(self):
        pass
