import unittest


class Judgement:

    def movelist_kin(self, sengo, suji, dan, koma):
        if sengo == 0:
            kin_list = [[suji + 1, dan - 1, koma], [suji, dan - 1, koma], [suji - 1, dan - 1, koma],
                        [suji + 1, dan, koma],
                        [suji - 1, dan, koma], [suji, dan + 1, koma]]
            print(kin_list)
            for list in kin_list:
                if 0 in list or 10 in list:
                    kin_list.remove(list)
        return kin_list


class MyTestCase(unittest.TestCase):
    def test_金の動ける範囲を返す(self):
        expected = [[2, 1, '金'], [1, 2, '金'], ]
        sashite = Judgement()
        actual = sashite.movelist_kin(0, 1, 1, "金")
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
