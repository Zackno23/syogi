import unittest


class Syogiban2sfen(object):
    def sfen(self, shogiban, turn, mochigoma_me, mochigoma_opponent):
        sfen = ''
        empty_count = 0
        for dan in range(len(shogiban)):
            for masume in range(len(shogiban[dan])):
                # マス目に駒がなかった場合の処理
                if shogiban[dan][masume][1] == "＊":
                    empty_count += 1
                elif shogiban[dan][masume][1] != "＊" and empty_count != 0:
                    sfen = sfen + str(empty_count) \
                           + Syogiban2sfen.piece_sfen(self, shogiban[dan][masume][0], shogiban[dan][masume][1])
                    empty_count = 0
                # 一筋目のマス目が空だったとき、数字を出力する
                elif masume == 8 and empty_count != 0:
                    sfen = str(empty_count)
                    empty_count = 0
                else:
                    sfen = sfen + Syogiban2sfen.piece_sfen(self, shogiban[dan][masume][0], shogiban[dan][masume][1])
            if empty_count != 0:
                sfen = sfen + str(empty_count)
            sfen = sfen + "/"
            empty_count = 0
        sfen = sfen[:-1]  # 最後の/を削除

        if turn == 0:  # sfenの手番を指定
            sfen = sfen + " b"  # black
        elif turn == 1:
            sfen = sfen + " w"  # white

        if mochigoma_opponent == [] and mochigoma_me == []:
            sfen = sfen + " -"
        else:
            mochigoma_sfen_temp = []  # 一時的に持ち駒全部入りのリストを作る。例)先手が歩二枚の場合、2PでなくPPとなる
            if len(mochigoma_me) >= 1:
                list_turn = 0
                for koma in mochigoma_me:
                    mochigoma_sfen_temp.append(Syogiban2sfen.piece_sfen(self, list_turn, koma))
            if len(mochigoma_opponent) >= 1:
                list_turn = 1
                for koma in mochigoma_opponent:
                    mochigoma_sfen_temp.append(Syogiban2sfen.piece_sfen(self, list_turn, koma))
            # mochigoma_tempを正しいSFENにする:各アルファベットの数をカウントし、順番にならべる
            piece_list = ["R", "B", "G", "S", "N", "L", "P", "r", "b", "g", "s", "n", "l", "p"]
            mochigoma_sfen = ""
            for i in piece_list:
                mochigoma_sfen = mochigoma_sfen + Syogiban2sfen.mochigoma_makesfen(self, mochigoma_sfen_temp.count(i),
                                                                                   i)
            sfen = sfen + " " + mochigoma_sfen

        sfen = sfen + " 1"  # おまじない
        return sfen

    def mochigoma_makesfen(self, num, koma):
        if num == 1:
            return koma
        elif num >= 2:
            return str(num) + koma
        else:
            return ""

    def piece_sfen(self, turn, piece):  # 駒のsfen記号への変換
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
        mochigoma_me = ["飛"]
        expected = "lnsgkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL b R2p 1"
        syogiban2sfen = Syogiban2sfen()
        actual = syogiban2sfen.sfen(shogiban, turn, mochigoma_me, mochigoma_opponent)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
