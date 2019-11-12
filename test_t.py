four_str = '1-2-3-4'
fr_list = four_str.split('-')
fc_all = tuple((x, fr_list[(fr_list.index(x) + 1) % 4]) for x in fr_list)
# print(fc_all)
print("U'2".strip("2'"))
ins_str = "234"
ins_all = ('u',)
for ins_s in ins_str:
    if '1' not in '1' and '2' not in '1':
        raise Exception('ins_str 含有其它字符')