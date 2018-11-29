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


def display(board):
    for dan in range(len(board)):
        for i in board[dan]:
            print(i[1], end="")
        print("")


display(shogiban)

turn = 0
while True:
    if (turn == 0 and len(mochigoma_me) > 0) or (turn == 1 and len(mochigoma_opponent) > 0):
        question_drop = input("持ち駒を使いますか?(y/n)")
        if question_drop.lower() == 'y':
            drop = input('どの駒を使いますか?')
            print("移動先")
            goal_Suji = int(input("筋"))
            goal_Dan = int(input("段"))
            if shogiban[goal_Dan - 1][9 - goal_Suji] != [2, "＊"]:
                print("不正な指し手です")
            shogiban[goal_Dan - 1][9 - goal_Suji] = [0, drop]
            if turn == 0:
                num = mochigoma_me.index([0, drop])
                mochigoma_me.pop(num)
            elif turn == 1:
                num = mochigoma_opponent.index([0, drop])
                mochigoma_opponent.pop(num)

            if turn == 0:
                turn = 1
            elif turn == 1:
                turn = 0
            print(mochigoma_opponent)
            display(shogiban)
            print(mochigoma_me)
            continue



    Origin_Suji = int(input("筋"))
    Origin_Dan = int(input("段"))
    koma = shogiban[Origin_Dan - 1][9 - Origin_Suji]

    if shogiban[Origin_Dan - 1][9 - Origin_Suji][0] == turn:
        print("移動先")
        goal_Suji = int(input("筋"))
        goal_Dan = int(input("段"))
        moved = shogiban[goal_Dan - 1][9 - goal_Suji]

        if moved[0] != turn and moved[0] != 2:
            moved[0] = turn
            if turn == 0:
                mochigoma_me.append(moved)
            else:
                mochigoma_opponent.append(moved)

        shogiban[Origin_Dan - 1][9 - Origin_Suji] = [2, '＊']
        shogiban[goal_Dan - 1][9 - goal_Suji] = koma

        if turn == 0:
            turn = 1
        elif turn == 1:
            turn = 0
    else:
        print("不正な指し手です。")
        continue

    print(mochigoma_opponent)
    display(shogiban)
    print(mochigoma_me)
