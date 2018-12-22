import unittest

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
mochigoma_opponent = ["歩", "歩"]
mochigoma_me = ["飛車"]


class Syogiban2sfen(object):
    def sfen(self):
        sfen = ''
        empty_count = 0
        for dan in range(len(shogiban)):
            for masume in range(len(shogiban[dan])):
                if shogiban[dan][masume][1] == "＊":
                    empty_count += 1
                elif shogiban[dan][masume][1] != "＊" and empty_count != 0:
                    sfen = sfen + str(empty_count) + Syogiban2sfen.piece_sfen(self, shogiban[dan][masume][0],
                                                                              shogiban[dan][masume][1])
                    empty_count = 0
                elif masume == 8 and empty_count != 0:
                    sfen = str(empty_count)
                    empty_count = 0
                else:
                    sfen = sfen + Syogiban2sfen.piece_sfen(self, shogiban[dan][masume][0], shogiban[dan][masume][1])
            if empty_count != 0:
                sfen = sfen + str(empty_count)
            sfen = sfen + "/"
            empty_count = 0
        sfen = sfen[:-1]

        if turn == 0:
            sfen = sfen + " b"
        elif turn == 1:
            sfen = sfen + " w"

        if mochigoma_opponent == [] and mochigoma_me == []:
            sfen = sfen + " -"
        else:
            mochigoma_sfen = []
            for koma in mochigoma_me:
                if koma == "歩":
                    mochigoma_sfen.append("P")
                if koma == "香":
                    mochigoma_sfen.append("L")
                if koma == "桂":
                    mochigoma_sfen.append("N")
                if koma == "銀":
                    mochigoma_sfen.append("S")
                if koma == "飛":
                    mochigoma_sfen.append("R")
                if koma == "角":
                    mochigoma_sfen.append("B")
            for koma in mochigoma_opponent:
                if koma == "歩":
                    mochigoma_sfen.append("p")
                if koma == "香":
                    mochigoma_sfen.append("l")
                if koma == "桂":
                    mochigoma_sfen.append("n")
                if koma == "銀":
                    mochigoma_sfen.append("s")
                if koma == "飛":
                    mochigoma_sfen.append("r")
                if koma == "角":
                    mochigoma_sfen.append("b")


        sfen = sfen + " 1"
        return sfen

    # 持ち駒の表示順序はとりあえずK → R → B → G → S → N → L → P → k → r → b → g → s → n → l → pにしてみよう
    # それぞれの駒を持ち駒リストから探索する必要がある
    # つまり引数として必要なのは、盤面、それぞれの持ち駒リスト、手番の4つ?
    # https://ch.nicovideo.jp/kifuwarabe/blomaga/ar795371
    # http://shogidokoro.starfree.jp/usi.html
    def mochigoma_count(self, list, koma):

    def piece_sfen(self, turn, piece):
        sfen_piece = ""
        if piece == "歩" or piece == "と":
            sfen_piece = "p"
        elif piece == "香" or piece == "杏":
            sfen_piece = "l"
        elif piece == "桂" or piece == "圭":
            sfen_piece = "n"
        elif piece == "銀" or piece == "全":
            sfen_piece = "s"
        elif piece == "金":
            sfen_piece = "g"
        elif piece == "飛" or piece == "龍":
            sfen_piece = "r"
        elif piece == "角" or piece == "馬":
            sfen_piece = "b"
        elif piece == "玉":
            sfen_piece = "k"

        if turn == 0:
            sfen_piece = sfen_piece.upper()

        if piece == 'と' or piece == '杏' or piece == '圭' or piece == '全' or piece == '龍' or piece == '馬':
            sfen_piece = "+" + sfen_piece
        return sfen_piece


class MyTestCase(unittest.TestCase):
    def test_初形を入力し初形のsfenを返す_手番はとりあえず手前側つまりblack(self):
        expected = "lnsgkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL b - 1"
        syogiban2sfen = Syogiban2sfen()
        actual = syogiban2sfen.sfen()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
