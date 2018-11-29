import unittest


class Judgement:
    def movelist_FU(self, sengo, suji, dan, koma):
        if sengo == 0:
            if dan > 1:
                return [[suji, dan - 1, koma]]
            elif dan == 1:
                return False
        elif sengo == 1:
            if dan < 9:
                return [suji, dan + 1, koma]
            elif dan == 9:
                return False

    def movelist_kyo(self, sengo, suji, dan, koma):
        kyo_list = []
        if sengo == 0:
            if dan != 1:
                for i in range(dan - 1):
                    kyo_list.append([suji, i + 1, koma])
            else:
                return False
        elif sengo == 1:
            if dan != 9:
                for i in range(9 - dan - 1):
                    kyo_list.append([suji, dan + 1 + i, koma])
            else:
                return False
        return kyo_list

    def movelist_kei(self, sengo, suji, dan, koma):
        if sengo == 0:
            if dan == 1 or dan == 2:
                return False
            if suji == 1:
                return [[suji + 1, dan - 2, koma]]
            elif suji == 9:
                return [[suji - 1, dan - 2, koma]]
            else:
                return [[suji - 1, dan - 2, koma], [suji + 1, dan - 2, koma]]
        elif sengo == 1:
            if dan == 8 or dan == 9:
                return False
            if suji == 1:
                return [[suji + 1, dan + +2, koma]]
            elif suji == 9:
                return [[suji - 1, dan + 2, koma]]
            else:
                return [[suji + 1, dan + 2, koma], [suji - 1, dan + 2, koma]]

    def movelist_gin(self, sengo, suji, dan, koma):
        if suji ==




class MyTestCase(unittest.TestCase):

    def test_符号を入力したときの歩の動ける範囲を返す_先後判定あり(self):
        expected = [[4, 1, '歩']]
        cyakusyu = Judgement()
        actual = cyakusyu.movelist_FU(0, 4, 2, "歩")
        self.assertEqual(expected, actual)

    def test_香車の動ける範囲を返す_先後判定あり(self):
        expected = [[2, 1, '香'], [2, 2, "香"], [2, 3, "香"], [2, 4, "香"], [2, 5, "香"], [2, 6, "香"], [2, 7, "香"], ]
        sashite = Judgement()
        actual = sashite.movelist_kyo(0, 2, 8, "香")
        self.assertEqual(expected, actual)

    def test_桂馬の動ける範囲を返す_先後判定あり(self):
        expected = [[3, 4, "桂"], [1, 4, "桂"]]
        sashite = Judgement()
        actual = sashite.movelist_kei(1, 2, 2, "桂")
        self.assertEqual(expected, actual)

    def test_銀の動ける範囲を返す(self):
        expected = [[6, 4, '銀'], [5, 4, '銀'], [4, 4, '銀'], [6, 6, '銀'], [4, 6, '銀']]
        sashite = Judgement()
        actual = sashite.movelist_gin(0, 5, 5, "銀")
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
