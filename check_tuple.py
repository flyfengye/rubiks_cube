def get_judge_tb(_src_list):
    _tb = dict()
    _tb['clockwise'] = tuple((i, 1) for i in _src_list[0].split('|'))  # 最后写成生成器对象看效率,生成器无法相加
    _tb['clockwise'] += tuple((i, 0) for i in _src_list[1].split('|'))
    _tb['clockwise'] += tuple((i, -1) for i in _src_list[2].split('|'))
    _tb['clockwise'] = set(_tb['clockwise'])
    _tb['anticlockwise'] = set((i.rstrip("'") if "'" in i else i + "'", n) for i, n in _tb['clockwise'])
    # _tb['turn_twice'] = tuple((i + "2", n) for i, n in _tb['clockwise'])
    # _tb['turn_twice'] += tuple((i + "2", n) for i, n in _tb['anticlockwise'])
    # _tb['turn_twice'] = set(_tb['turn_twice'])
    return _tb


__ud = ["U|u|y", "E'|u|d'|y", "D'|d'|y"]
__rl = ["R|r|x", "M'|r|l'|x", "L'|l'|x"]
__fb = ["B'|b'|z'", "S'|b'|f|z'", "F|f|z'"]
UD = get_judge_tb(__ud)
RL = get_judge_tb(__rl)
FB = get_judge_tb(__fb)


if __name__ == '__main__':
    from pprint import pprint

    ud_bak = {
        'clockwise': (
            ("U", 1), ("D'", -1), ("E'", 0),
            ("u", 1), ("u", 0), ("d'", -1), ("d'", 0),
            ("y", 1), ("y", 0), ("y", -1)
        ),
        'anticlockwise': (
            ("U'", 1), ("D", -1), ("E", 0),
            ("u'", 1), ("u'", 0), ("d", -1), ("d", 0),
            ("y'", 1), ("y'", 0), ("y'", -1)
        ),
        'turn_twice': (
            ("U2", 1), ("U'2", 1), ("D2", -1), ("D'2", -1), ("E2", 0), ("E'2", 0),
            ("u2", 1), ("u2", 0), ("d'2", -1), ("d'2", 0), ("u'2", 1), ("u'2", 0), ("d2", -1), ("d2", 0),
            ("y'2", 1), ("y'2", 0), ("y'2", -1), ("y2", 1), ("y2", 0), ("y2", -1)
        )
    }

    # ud = get_judge_tb(__ud)
    # rl = get_judge_tb(__rl)
    fb = get_judge_tb(__fb)

    # pprint(ud)
    # pprint(rl)
    pprint(fb)
