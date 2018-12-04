


class Judgement:
    def movelist_FU(self, sengo, suji, dan, koma):
        if sengo == 0:
            if dan > 1:
                return [[suji, dan - 1, koma]]
            elif dan == 1:
                return []
        elif sengo == 1:
            if dan < 9:
                return [[suji, dan + 1, koma]]
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
