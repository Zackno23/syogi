import unittest


class Judgement:

    def movelist_kin(self, sengo, suji, dan, koma):
        if sengo == 0:
            kin_list = [[suji + 1, dan - 1, koma], [suji, dan - 1, koma], [suji - 1, dan - 1, koma],
                        [suji + 1, dan, koma],
                        [suji - 1, dan, koma], [suji, dan + 1, koma]]
            print(kin_list)

            return hoge(kin_list)

            for list in kin_list:
                if 0 in list or 10 in list:
                    kin_list.remove(list)

        return kin_list


def hoge(kin_list):
    valid_list = []
    for x in kin_list:
        if 0 not in x:
            valid_list.append(x)
    return valid_list

    # return [x for x in kin_list if not 0 in x]


class MyTestCase(unittest.TestCase):
    def test_金の動ける範囲を返す(self):
        expected = [[2, 1, '金'], [1, 2, '金'], ]
        sashite = Judgement()
        actual = sashite.movelist_kin(0, 1, 1, "金")
        self.assertEqual(expected, actual)

    def test_01(self):
        kin_list = [[2, 0, '金'],
                    [1, 0, '金'],
                    [0, 0, '金'],
                    [2, 1, '金'],
                    [0, 1, '金'],
                    [1, 2, '金']]

        expected = [[2, 1, '金'], [1, 2, '金'], ]

        actual = hoge(kin_list)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
