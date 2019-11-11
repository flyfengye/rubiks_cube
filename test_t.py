four_str = '1-2-3-4'
fr_list = four_str.split('-')
fc_all = tuple((x, fr_list[(fr_list.index(x) + 1) % 4]) for x in fr_list)
print(fc_all)