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
        for i in range(dan - 1):
            kyo_list.append([suji, i + 1, koma])
        return kyo_list


class MyTestCase(unittest.TestCase):

    def test_符号を入力したときの歩の動ける範囲を返す_先後判定あり(self):
        expected = [[4, 1, '歩']]
        cyakusyu = Judgement()
        actual = cyakusyu.movelist_FU(0, 4, 2, "歩")
        self.assertEqual(expected, actual)

    def test_香車の動ける範囲を返す_先後判定あり(self):
        expected = [[1, 1, '香'], [1, 2, "香"], [1, 3, "香"], [1, 4, '香']]
        sashite = Judgement()
        actual = sashite.movelist_kyo(0, 1, 5, "香")
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
