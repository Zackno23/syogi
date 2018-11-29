import unittest


class Judgement:
    def movelist(self, suji, dan, koma):
        if dan > 1:
            return [suji, dan - 1, koma]
        if dan == 1:
            return False


class MyTestCase(unittest.TestCase):

    def test_符号を入力したときの歩の動ける範囲を返す_先後判定なし(self):
        expected = [4, 1, '歩']
        cyakusyu = Judgement()
        actual = cyakusyu.movelist(4, 2, "歩")
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
