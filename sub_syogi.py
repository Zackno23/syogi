dan0 = [[1, '香'], [1, '桂'], [1, '銀'], [1, '金'], [1, "玉"], [1, '金'], [1, '銀'], [1, '桂'], [1, '香']]
dan1 = [[2, '＊'], [1, '飛'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [1, '角'], [2, '＊']]
dan2 = [[1, '歩'], [1, '歩'], [1, '歩'], [1, '歩'], [1, '歩'], [1, '歩'], [1, '歩'], [1, '歩'], [1, '歩']]
dan3 = [[2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊']]
dan4 = [[2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊']]
dan5 = [[2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊']]
dan6 = [[0, '歩'], [0, '歩'], [0, '歩'], [0, '歩'], [0, '歩'], [0, '歩'], [0, '歩'], [0, '歩'], [0, '歩']]
dan7 = [[2, '＊'], [0, '角'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [0, '飛'], [2, '＊']]
dan8 = [[0, '香'], [0, '桂'], [0, '銀'], [0, '金'], [0, "玉"], [0, '金'], [0, '銀'], [0, '桂'], [0, '香']]

shogiban = [dan0, dan1, dan2, dan3, dan4, dan5, dan6, dan7, dan8]
mochigoma_opponent = []
mochigoma_me = []

for dan in range(len(shogiban)):
    for i in shogiban[dan]:
        print(i[1], end="")
    print("")

turn = 0
while True:
    print("移動元")
    Origin_Suji = int(input("筋"))
    Origin_Dan = int(input("段"))
    print("移動先")
    goal_Suji = int(input("筋"))
    goal_Dan = int(input("段"))

    if shogiban[Origin_Dan - 1][9 - Origin_Suji][0] == turn:
        koma = shogiban[Origin_Dan - 1][9 - Origin_Suji]
        moved = shogiban[goal_Dan - 1][9 - goal_Suji]

        if moved[0] != turn and moved[0] != 2:
            moved[0] = turn
            if turn == 0:
                mochigoma_me.append(moved)
            else:
                mochigoma_opponent.append(moved)

        koma = [2, '＊']
        moved = koma


        if turn == 0:
            turn = 1
        elif turn == 1:
            turn = 0
    else:
        print("不正な着手です。")
        continue

    print(mochigoma_opponent)
    for dan in range(len(shogiban)):
        for i in shogiban[dan]:
            print(i[1], end="")
        print("")
    print(mochigoma_me)
