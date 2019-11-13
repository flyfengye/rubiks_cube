four_str = '1-2-3-4'
fr_list = four_str.split('-')
fc_all = tuple((x, fr_list[(fr_list.index(x) + 1) % 4]) for x in fr_list)
# print(fc_all)
# print("U'2".strip("2'"))
# ins_str = "234"
# ins_all = ('u',)
# for ins_s in ins_str:
#     if '1' not in '1' and '2' not in '1':
#         raise Exception('ins_str 含有其它字符')
a = (('1', '2'), (('3', '4'), ('5', '6')))
c = (('1', '2'), {('3', '4'), ('5', '6')})
b = set()
# c = a[1][0]
# print(c)
for i in a[0]:
    for m in a[1][0]:
        for n in a[1][1]:
            print((i, m, n))

for i in c[0]:
    for j in c[1]:
        print((i,) + j)


order = [('a', 'd'), ('c', 'f'), ('b',)]
u, d, f, b, r, l = (0, 'u', 1), (0, 'd', -1), (1, 'f', -1), (1, 'b', 1), (2, 'r', 1), (2, 'l', -1)
def get_pos(*args):
    pos = [0, 0, 0]
    for arg in args:
        pos[arg[0]] = arg[2]
    return pos
c1 = ((u, d), ((b, f), (r, l)))
c2 = ((u, d), (b, f, r, l))
c3 = (u, d, b, f, r, l)
c3 = (get_pos(x) for x in c3)
print(tuple(c3))
# 角
# (u, d), ((b, f), (r, l))
# (1, 1, 1), (u, b, r)
# (1, -1, 1), (u, f, r)
# (-1, -1, 1), (u, f, l)
# (-1, 1, 1), (u, b, l)
#
# (1, 1, -1), (d, b, r)
# (1, -1, -1), (d, f, r)
# (-1, -1, -1), (d, f, l)
# (-1, 1, -1), (d, b, l)
#
# 棱
# ((u, d), (b, f, r, l))
# (1, 0, 1), (u, '', r)
# (0, -1, 1), (u, f, '')
# (-1, 0, 1), (u, '', l)
# (0, 1, 1), (u, b, '')
#
# (1, 1, 0), ('', b, r)
# (1, -1, 0), ('', f, r)
# (-1, -1, 0), ('', f, l)
# (-1, 1, 0), ('', b, l)
#
#
# 中心
# (u, d), ((b, f), (r, l))
# (1, 0, 0), ('', '', r)
# (0, -1, 0), ('', f, '')
# (-1, 0, 0), ('', '', l)
# (0, 1, 0), ('', b, '')
# (0, 0, 1), (u, '', '')
# (0, 0, -1), (d, '', '')
#