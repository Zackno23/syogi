import unittest


class Judgement:
    def movelist_FU(self, sengo, suji, dan, koma):
        if sengo == 0:
            if dan > 1:
                return [[suji, dan - 1, koma]]
            elif dan == 1:
                return []
        elif sengo == 1:
            if dan < 9:
                return [suji, dan + 1, koma]
            elif dan == 9:
                return []

    def movelist_kyo(self, sengo, suji, dan, koma):
        valid_list = []
        if sengo == 0:
            if dan != 1:
                for i in range(dan - 1):
                    valid_list.append([suji, i + 1, koma])
            else:
                []
        elif sengo == 1:
            if dan != 9:
                for i in range(9 - dan - 1):
                    valid_list.append([suji, dan + 1 + i, koma])
            else:
                return []
        return valid_list

    def movelist_kei(self, sengo, suji, dan, koma):
        if sengo == 0:
            if dan == 1 or dan == 2:
                return []
            if suji == 1:
                return [[suji + 1, dan - 2, koma]]
            elif suji == 9:
                return [[suji - 1, dan - 2, koma]]
            else:
                return [[suji - 1, dan - 2, koma], [suji + 1, dan - 2, koma]]
        elif sengo == 1:
            if dan == 8 or dan == 9:
                return []
            if suji == 1:
                return [[suji + 1, dan + +2, koma]]
            elif suji == 9:
                return [[suji - 1, dan + 2, koma]]
            else:
                return [[suji + 1, dan + 2, koma], [suji - 1, dan + 2, koma]]

    def movelist_gin(self, sengo, suji, dan, koma):
        if sengo == 0:
            gin_list = [[suji + 1, dan - 1, koma],
                        [suji, dan - 1, koma],
                        [suji - 1, dan - 1, koma],
                        [suji + 1, dan + 1, koma],
                        [suji - 1, dan + 1, koma]]
        elif sengo == 1:
            gin_list = [[suji + 1, dan - 1, koma],
                        [suji - 1, dan - 1, koma],
                        [suji + 1, dan + 1, koma],
                        [suji, dan + 1, koma],
                        [suji - 1, dan + 1, koma]]

        valid_list = []
        for x in gin_list:

            no_ten = 10 not in x
            no_zero = 0 not in x

            if no_ten and no_zero:
                valid_list.append(x)

        return valid_list

    def movelist_kin(self, sengo, suji, dan, koma):
        if sengo == 0:
            kin_list = [[suji + 1, dan - 1, '金'],
                        [suji, dan - 1, '金'],
                        [suji - 1, dan - 1, '金'],
                        [suji + 1, dan, '金'],
                        [suji - 1, dan, '金'],
                        [suji, dan + 1, '金']]
        elif sengo == 1:
            kin_list = [[suji, dan - 1, '金'],
                        [suji + 1, dan, '金'],
                        [suji - 1, dan, '金'],
                        [suji + 1, dan + 1, '金'],
                        [suji, dan + 1, '金'],
                        [suji - 1, dan + 1, '金']]
        valid_list = []
        for x in kin_list:
            no_ten = 10 not in x
            no_zero = 0 not in x

            if no_ten and no_zero:
                valid_list.append(x)

        return valid_list

        return kin_list

    def movelist_KAKU(self, sengo, suji, dan, koma):
        valid_list = []
        kaku_suji = suji
        kaku_dan = dan
        while (2 <= kaku_suji <= 8) and (2 <= kaku_dan <= 8):
            valid_list.append([kaku_suji - 1, kaku_dan - 1, koma])
            kaku_suji = kaku_suji - 1
            kaku_dan = kaku_dan - 1
        kaku_suji = suji
        kaku_dan = dan
        while (2 <= kaku_suji <= 8) and (2 <= kaku_dan <= 8):
            valid_list.append([kaku_suji + 1, kaku_dan - 1, koma])
            kaku_suji = kaku_suji + 1
            kaku_dan = kaku_dan - 1
        kaku_suji = suji
        kaku_dan = dan
        while (2 <= kaku_suji <= 8) and (2 <= kaku_dan <= 8):
            valid_list.append([kaku_suji + 1, kaku_dan + 1, koma])
            kaku_suji = kaku_suji + 1
            kaku_dan = kaku_dan + 1
        kaku_suji = suji
        kaku_dan = dan
        while (2 <= kaku_suji <= 8) and (2 <= kaku_dan <= 8):
            valid_list.append([kaku_suji - 1, kaku_dan + 1, koma])
            kaku_suji = kaku_suji - 1
            kaku_dan = kaku_dan + 1
        return valid_list

    def movelist_HISYA(self, sengo, suji, dan, koma):
        valid_list = []
        kaku_suji = suji
        kaku_dan = dan
        while (2 <= kaku_suji <= 8) and (2 <= kaku_dan <= 8):
            valid_list.append([kaku_suji - 1, kaku_dan, koma])
            kaku_suji = kaku_suji - 1
        kaku_suji = suji
        kaku_dan = dan
        while (2 <= kaku_suji <= 8) and (2 <= kaku_dan <= 8):
            valid_list.append([kaku_suji, kaku_dan - 1, koma])
            kaku_dan = kaku_dan - 1
        kaku_suji = suji
        kaku_dan = dan
        while (2 <= kaku_suji <= 8) and (2 <= kaku_dan <= 8):
            valid_list.append([kaku_suji + 1, kaku_dan, koma])
            kaku_suji = kaku_suji + 1
        kaku_suji = suji
        kaku_dan = dan
        while (2 <= kaku_suji <= 8) and (2 <= kaku_dan <= 8):
            valid_list.append([kaku_suji, kaku_dan + 1, koma])
            kaku_dan = kaku_dan + 1
        return valid_list

    def movelist_GYOKU(self, sengo, suji, dan, koma):
        gyoku_list = [[suji + 1, dan - 1, '玉'],
                      [suji, dan - 1, '玉'],
                      [suji - 1, dan - 1, '玉'],
                      [suji + 1, dan, '玉'],
                      [suji - 1, dan, '玉'],
                      [suji + 1, dan + 1, "玉"],
                      [suji, dan + 1, '玉'],
                      [suji - 1, dan + 1, "玉"]]
        valid_list = []
        for x in gyoku_list:
            no_ten = 10 not in x
            no_zero = 0 not in x

            if no_ten and no_zero:
                valid_list.append(x)

        return valid_list


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

    def test_銀の動ける範囲を返す_先後判定あり(self):
        expected = [[2, 2, '銀'], [1, 2, "銀"]]
        sashite = Judgement()
        actual = sashite.movelist_gin(1, 1, 1, "銀")
        self.assertEqual(expected, actual)

    def test_金の動ける範囲を返す(self):
        expected = [[8, 1, '金'], [9, 2, '金'], [8, 2, '金']]
        sashite = Judgement()
        actual = sashite.movelist_kin(1, 9, 1, "金")
        self.assertEqual(expected, actual)

    def test_角の動ける範囲を返す(self):
        sashite = Judgement()
        expected = [[4, 4, '角'],
                    [3, 3, '角'],
                    [2, 2, '角'],
                    [1, 1, '角'],
                    [6, 4, '角'],
                    [7, 3, '角'],
                    [8, 2, '角'],
                    [9, 1, '角'],
                    [6, 6, '角'],
                    [7, 7, '角'],
                    [8, 8, '角'],
                    [9, 9, '角'],
                    [4, 6, '角'],
                    [3, 7, '角'],
                    [2, 8, '角'],
                    [1, 9, '角']]
        actual = sashite.movelist_KAKU(0, 5, 5, "角")
        self.assertEqual(expected, actual)

    def test_飛車の動ける範囲を返す(self):
        sashite = Judgement()
        expected = [[4, 5, "飛"], [3, 5, "飛"], [2, 5, "飛"], [1, 5, "飛"], [5, 4, "飛"], [5, 3, "飛"], [5, 2, "飛"],
                    [5, 1, "飛"], [6, 5, "飛"], [7, 5, "飛"], [8, 5, "飛"], [9, 5, "飛"], [5, 6, "飛"], [5, 7, "飛"],
                    [5, 8, "飛"], [5, 9, "飛"]]

        actual = sashite.movelist_HISYA(0, 5, 5, '飛')
        self.assertEqual(expected, actual)

    def test_玉の動ける範囲を返す(self):
        sashite = Judgement()
        expected = [[6, 4, "玉"], [5, 4, "玉"], [4, 4, "玉"], [6, 5, "玉"], [4, 5, "玉"], [6, 6, "玉"], [5, 6, "玉"],
                    [4, 6, "玉"]]
        actual = sashite.movelist_GYOKU(0, 5, 5, '玉')
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
