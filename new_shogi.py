import random

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

turn = 0
CPUの持ち駒 = []
プレーヤーの持ち駒 = []
"""
先手後手の選定
プレーヤー側を手前にする
振り駒システム
プレーヤーターン中にやること
1持ち駒を使うかの選択→持ち駒の処理
2指す駒の選択
3移動先の選択
4相手の駒を取るときの処理
5成り駒の処理
6王手がかかっていたときの処理
・玉の動けることろリストからいろいろ削除
・outeをtrueにする
sfen表記に変換
API使ってコンピュータのの手を指す
"""


# 先手、後手の判定 0が先手
def furigoma():
    振り駒 = random.randint(0, 1)
    if 振り駒 == 0:
        player = 0
        computer = 1
    else:
        playter = 1
        computer = 0


def display(board):
    if len(CPUの持ち駒) > 0:
        for i in CPUの持ち駒:
            print(i)
    for dan in range(len(board)):
        for i in board[dan]:
            print(i[1], end="")
        print("")
    if len(プレーヤーの持ち駒) > 0:
        for i in プレーヤーの持ち駒:
            print(i)


def main():
    pass


if __name__ == "__main__":
    furigoma()
    display(shogiban)
    main()
