default = [['ABE', 'BE', 'BCE', 'CE', 'CDE', 'DE', 'DAE', 'AE', 'E'],
           ['AB', 'B', 'BC', 'C', 'CD', 'D', 'DA', 'A', ''],
           ['ABF', 'BF', 'BCF', 'CF', 'CDF', 'DF', 'DAF', 'AF', 'F']]


class CornerPieces:
    def __init__(self):
        self.position = (1, 1, 1)

    def turn(self, ins_str):
        x, y, z = self.position

        if (ins_str == "U" and z == 1) or (ins_str == "D'" and z == -1):
            x, y = self.__clockwise((x, y))
        elif (ins_str == "U'" and z == 1) or (ins_str == "D" and z == -1):
            x, y = self.__anticlockwise((x, y))

        elif (ins_str == "R" and x == 1) or (ins_str == "L'" and x == -1):
            y, z = self.__clockwise((y, z))
        elif (ins_str == "R'" and x == 1) or (ins_str == "L" and x == -1):
            y, z = self.__anticlockwise((y, z))

        elif (ins_str == "F" and y == -1) or (ins_str == "B'" and y == 1):
            x, z = self.__clockwise((x, z))
        elif (ins_str == "F'" and y == -1) or (ins_str == "B" and y == 1):
            x, z = self.__anticlockwise((x, z))

        self.position = (x, y, z)

    @staticmethod
    def __clockwise(_pos, counter=1):
        df = ((1, 1), (1, -1), (-1, -1), (-1, 1))
        return df[(df.index(_pos) + counter) % 4]

    @staticmethod
    def __anticlockwise(_pos, counter=1):
        df = ((1, 1), (-1, 1), (-1, -1), (1, -1))
        return df[(df.index(_pos) + counter) % 4]


class EdgePieces:
    def __init__(self):
        pass


class CenterPieces:
    def __init__(self):
        pass


if __name__ == '__main__':
    crn = CornerPieces()
    crn.position = (1, 1, 1)
    crn.turn("B'")
    print(crn.position)