def hoge(kin_list):
    valid_list = []

    for x in kin_list:

        no_ten = 10 not in x
        no_zero = 0 not in x

        if no_ten and no_zero:
            valid_list.append(x)

    return valid_list


kin_list = [[10, 8, '金'],
            [9, 8, '金'],
            [8, 8, '金'],
            [10, 9, '金'],
            [0, 9, '金'],
            [9, 10, '金']]

print(hoge(kin_list))
