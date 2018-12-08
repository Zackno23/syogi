class Judgement_gogo:
    def movelist_FU(self, sengo, suji, dan, koma):
        if sengo == 0:
            if dan > 1:
                return [[suji, dan - 1, koma]]
            elif dan == 1:
                return []
        elif sengo == 1:
            if dan < 5:
                return [[suji, dan + 1, koma]]
            elif dan == 5:
                return []

    def movelist_kyo(self, sengo, suji, dan, koma, sente_list, gote_list):
        valid_list = []
        if sengo == 0:
            if dan != 1:
                for i in range(dan - 1):
                    if [suji, 4 - i] in sente_list:
                        break
                    elif [suji, 4 - 1] in gote_list:
                        valid_list.append([suji, 4 - i, koma])
                        break
                    else:
                        valid_list.append([suji, 4 - i, koma])
            else:
                return []
        elif sengo == 1:
            if dan != 5:
                for i in range(4 - dan):
                    if [suji, dan + 1 + i] in sente_list:
                        valid_list.append([[suji, dan + 1 + i], koma])
                    elif [suji, dan + 1 + i] in gote_list:
                        break
                    else:
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
            elif suji == 5:
                return [[suji - 1, dan - 2, koma]]
            else:
                return [[suji - 1, dan - 2, koma], [suji + 1, dan - 2, koma]]
        elif sengo == 1:
            if dan == 4 or dan == 5:
                return []
            if suji == 1:
                return [[suji + 1, dan + +2, koma]]
            elif suji == 5:
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

            no_ten = 6 not in x
            no_zero = 0 not in x

            if no_ten and no_zero:
                valid_list.append(x)

        return valid_list

    def movelist_kin(self, sengo, suji, dan, koma):
        if sengo == 0:
            kin_list = [[suji + 1, dan - 1, koma],
                        [suji, dan - 1, koma],
                        [suji - 1, dan - 1, koma],
                        [suji + 1, dan, koma],
                        [suji - 1, dan, koma],
                        [suji, dan + 1, koma]]
        elif sengo == 1:
            kin_list = [[suji, dan - 1, koma],
                        [suji + 1, dan, koma],
                        [suji - 1, dan, koma],
                        [suji + 1, dan + 1, koma],
                        [suji, dan + 1, koma],
                        [suji - 1, dan + 1, koma]]
        valid_list = []
        for x in kin_list:
            no_ten = 6 not in x
            no_zero = 0 not in x

            if no_ten and no_zero:
                valid_list.append(x)

        return valid_list

    def movelist_KAKU(self, sengo, suji, dan, koma, sente_list, gote_list):
        valid_list = []
        kaku_suji = suji
        kaku_dan = dan
        while (1 <= kaku_suji <= 5) and (1 <= kaku_dan <= 5):
            if kaku_suji == 1 or kaku_dan == 1:
                break
            if sengo == 0:
                if [kaku_suji - 1, kaku_dan - 1] in sente_list:
                    break
                elif [kaku_suji - 1, kaku_dan - 1] in gote_list:
                    valid_list.append([kaku_suji - 1, kaku_dan - 1, koma])
                    break
                else:
                    valid_list.append([kaku_suji - 1, kaku_dan - 1, koma])
            if sengo == 1:
                if [kaku_suji - 1, kaku_dan - 1] in sente_list:
                    valid_list.append([kaku_suji - 1, kaku_dan - 1, koma])
                    break
                elif [kaku_suji - 1, kaku_dan - 1] in gote_list:
                    break
                else:
                    valid_list.append([kaku_suji - 1, kaku_dan - 1, koma])

            kaku_suji = kaku_suji - 1
            kaku_dan = kaku_dan - 1
        kaku_suji = suji
        kaku_dan = dan

        while (1 <= kaku_suji <= 5) and (1 <= kaku_dan <= 5):
            if kaku_suji == 5 or kaku_dan == 1:
                break
            if sengo == 0:
                if [kaku_suji + 1, kaku_dan - 1] in sente_list:
                    break
                elif [kaku_suji + 1, kaku_dan - 1] in gote_list:
                    valid_list.append([kaku_suji + 1, kaku_dan - 1, koma])
                    break
                else:
                    valid_list.append([kaku_suji + 1, kaku_dan - 1, koma])
            if sengo == 1:
                if [kaku_suji + 1, kaku_dan - 1] in sente_list:
                    valid_list.append([kaku_suji + 1, kaku_dan - 1, koma])
                    break
                elif [kaku_suji + 1, kaku_dan - 1] in gote_list:
                    break
                else:
                    valid_list.append([kaku_suji + 1, kaku_dan - 1, koma])

            kaku_suji = kaku_suji + 1
            kaku_dan = kaku_dan - 1
        kaku_suji = suji
        kaku_dan = dan
        while (1 <= kaku_suji <= 5) and (1 <= kaku_dan <= 5):
            if kaku_suji == 5 or kaku_dan == 5:
                break
            if sengo == 0:
                if [kaku_suji + 1, kaku_dan + 1] in sente_list:
                    break
                elif [kaku_suji + 1, kaku_dan + 1] in gote_list:
                    valid_list.append([kaku_suji + 1, kaku_dan + 1, koma])
                    break
                else:
                    valid_list.append([kaku_suji + 1, kaku_dan + 1, koma])
            if sengo == 1:
                if [kaku_suji + 1, kaku_dan + 1] in sente_list:
                    valid_list.append([kaku_suji + 1, kaku_dan + 1, koma])
                    break
                elif [kaku_suji + 1, kaku_dan + 1] in gote_list:
                    break
                else:
                    valid_list.append([kaku_suji + 1, kaku_dan + 1, koma])

            kaku_suji = kaku_suji + 1
            kaku_dan = kaku_dan + 1
        kaku_suji = suji
        kaku_dan = dan
        while (1 <= kaku_suji <= 5) and (1 <= kaku_dan <= 5):
            if kaku_suji == 1 or kaku_dan == 5:
                break
            if sengo == 0:
                if [kaku_suji - 1, kaku_dan + 1] in sente_list:
                    break
                elif [kaku_suji - 1, kaku_dan + 1] in gote_list:
                    valid_list.append([kaku_suji - 1, kaku_dan + 1, koma])
                    break
                else:
                    valid_list.append([kaku_suji - 1, kaku_dan + 1, koma])
            if sengo == 1:
                if [kaku_suji - 1, kaku_dan + 1] in sente_list:
                    valid_list.append([kaku_suji - 1, kaku_dan + 1, koma])
                    break
                elif [kaku_suji - 1, kaku_dan + 1] in gote_list:
                    break
                else:
                    valid_list.append([kaku_suji - 1, kaku_dan + 1, koma])

            kaku_suji = kaku_suji - 1
            kaku_dan = kaku_dan + 1

        return valid_list

    def movelist_HISYA(self, sengo, suji, dan, koma, sente_list, gote_list):
        valid_list = []
        hisya_suji = suji
        hisya_dan = dan

        while (1 <= hisya_suji <= 5) and (1 <= hisya_dan <= 5):
            if hisya_suji == 1:
                break
            if sengo == 0:

                if [hisya_suji - 1, hisya_dan] in sente_list:
                    break
                elif [hisya_suji - 1, hisya_dan] in gote_list:
                    valid_list.append([hisya_suji - 1, hisya_dan, koma])
                    break
                else:
                    valid_list.append([hisya_suji - 1, hisya_dan, koma])
            if sengo == 1:
                if [hisya_suji - 1, hisya_dan] in sente_list:
                    valid_list.append([hisya_suji - 1, hisya_dan, koma])
                    break
                elif [hisya_suji - 1, hisya_dan] in gote_list:
                    break
                else:
                    valid_list.append([hisya_suji - 1, hisya_dan, koma])

            hisya_suji = hisya_suji - 1
        hisya_suji = suji
        hisya_dan = dan

        while (1 <= hisya_suji <= 5) and (1 <= hisya_dan <= 5):
            if hisya_dan == 1:
                break
            if sengo == 0:
                if [hisya_suji, hisya_dan - 1] in sente_list:
                    break
                elif [hisya_suji, hisya_dan - 1] in gote_list:
                    valid_list.append([hisya_suji, hisya_dan - 1, koma])
                    break
                else:
                    valid_list.append([hisya_suji, hisya_dan - 1, koma])
            if sengo == 1:
                if [hisya_suji, hisya_dan - 1] in sente_list:
                    valid_list.append([hisya_suji, hisya_dan - 1, koma])
                    break
                elif [hisya_suji, hisya_dan - 1] in gote_list:
                    break
                else:
                    valid_list.append([hisya_suji, hisya_dan - 1, koma])

            hisya_dan = hisya_dan - 1
        hisya_suji = suji
        hisya_dan = dan
        while (1 <= hisya_suji <= 5) and (1 <= hisya_dan <= 5):
            if hisya_suji == 5:
                break
            if sengo == 0:
                if [hisya_suji + 1, hisya_dan] in sente_list:
                    break
                elif [hisya_suji + 1, hisya_dan] in gote_list:
                    valid_list.append([hisya_suji + 1, hisya_dan, koma])
                    break
                else:
                    valid_list.append([hisya_suji + 1, hisya_dan, koma])
            if sengo == 1:
                if [hisya_suji + 1, hisya_dan] in sente_list:
                    valid_list.append([hisya_suji + 1, hisya_dan, koma])
                    break
                elif [hisya_suji + 1, hisya_dan] in gote_list:
                    break
                else:
                    valid_list.append([hisya_suji + 1, hisya_dan, koma])

            hisya_suji = hisya_suji + 1
        hisya_suji = suji
        hisya_dan = dan
        while (1 <= hisya_suji <= 5) and (1 <= hisya_dan <= 5):
            if hisya_dan == 5:
                break
            if sengo == 0:
                if [hisya_suji, hisya_dan + 1] in sente_list:
                    break
                elif [hisya_suji, hisya_dan + 1] in gote_list:
                    valid_list.append([hisya_suji, hisya_dan + 1, koma])
                    break
                else:
                    valid_list.append([hisya_suji, hisya_dan + 1, koma])
            if sengo == 1:
                if [hisya_suji, hisya_dan + 1] in sente_list:
                    valid_list.append([hisya_suji, hisya_dan + 1, koma])
                    break
                elif [hisya_suji, hisya_dan + 1] in gote_list:
                    break
                else:
                    valid_list.append([hisya_suji, hisya_dan + 1, koma])

            hisya_suji = hisya_suji + 1
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
            no_ten = 6 not in x
            no_zero = 0 not in x

            if no_ten and no_zero:
                valid_list.append(x)

        return valid_list

    def movelist_UMA(self, sengo, suji, dan, koma, sente_list, gote_list):
        valid_list = []
        uma_suji = suji
        uma_dan = dan
        while (1 <= uma_suji <= 5) and (1 <= uma_dan <= 5):
            if uma_suji == 1 or uma_dan == 5:
                break
            if sengo == 0:
                if [uma_suji - 1, uma_dan - 1] in sente_list:
                    break
                elif [uma_suji - 1, uma_dan - 1] in gote_list:
                    valid_list.append([uma_suji - 1, uma_dan - 1, koma])
                    break
                else:
                    valid_list.append([uma_suji - 1, uma_dan - 1, koma])
            if sengo == 1:
                if [uma_suji - 1, uma_dan - 1] in sente_list:
                    valid_list.append([uma_suji - 1, uma_dan - 1, koma])
                    break
                elif [uma_suji - 1, uma_dan - 1] in gote_list:
                    break
                else:
                    valid_list.append([uma_suji - 1, uma_dan - 1, koma])

            uma_suji = uma_suji - 1
            uma_dan = uma_dan - 1
        uma_suji = suji
        uma_dan = dan

        while (1 <= uma_suji <= 5) and (1 <= uma_dan <= 5):
            if uma_suji == 5 or uma_suji == 1:
                break
            if sengo == 0:
                if [uma_suji + 1, uma_dan - 1] in sente_list:
                    break
                elif [uma_suji + 1, uma_dan - 1] in gote_list:
                    valid_list.append([uma_suji + 1, uma_dan - 1, koma])
                    break
                else:
                    valid_list.append([uma_suji + 1, uma_dan - 1, koma])
            if sengo == 1:
                if [uma_suji + 1, uma_dan - 1] in sente_list:
                    valid_list.append([uma_suji + 1, uma_dan - 1, koma])
                    break
                elif [uma_suji + 1, uma_dan - 1] in gote_list:
                    break
                else:
                    valid_list.append([uma_suji + 1, uma_dan - 1, koma])

            uma_suji = uma_suji + 1
            uma_dan = uma_dan - 1
        uma_suji = suji
        uma_dan = dan
        while (1 <= uma_suji <= 5) and (1 <= uma_dan <= 5):
            if uma_suji == 5 or uma_dan == 5:
                break
            if sengo == 0:
                if [uma_suji + 1, uma_dan + 1] in sente_list:
                    break
                elif [uma_suji + 1, uma_dan + 1] in gote_list:
                    valid_list.append([uma_suji + 1, uma_dan + 1, koma])
                    break
                else:
                    valid_list.append([uma_suji + 1, uma_dan + 1, koma])
            if sengo == 1:
                if [uma_suji + 1, uma_dan + 1] in sente_list:
                    valid_list.append([uma_suji + 1, uma_dan + 1, koma])
                    break
                elif [uma_suji + 1, uma_dan + 1] in gote_list:
                    break
                else:
                    valid_list.append([uma_suji + 1, uma_dan + 1, koma])

            uma_suji = uma_suji + 1
            uma_dan = uma_dan + 1
        uma_suji = suji
        uma_dan = dan
        while (1 <= uma_suji <= 5) and (1 <= uma_dan <= 5):
            if uma_suji == 1 or uma_dan == 5:
                break
            if sengo == 0:
                if [uma_suji - 1, uma_dan + 1] in sente_list:
                    break
                elif [uma_suji - 1, uma_dan + 1] in gote_list:
                    valid_list.append([uma_suji - 1, uma_dan + 1, koma])
                    break
                else:
                    valid_list.append([uma_suji - 1, uma_dan + 1, koma])
            if sengo == 1:
                if [uma_suji - 1, uma_dan + 1] in sente_list:
                    valid_list.append([uma_suji - 1, uma_dan + 1, koma])
                    break
                elif [uma_suji - 1, uma_dan + 1] in gote_list:
                    break
                else:
                    valid_list.append([uma_suji - 1, uma_dan + 1, koma])

            uma_suji = uma_suji - 1
            uma_dan = uma_dan + 1
        nari_list = [[uma_suji + 1, uma_dan, koma], [uma_suji - 1, uma_dan, koma], [uma_suji, uma_dan + 1, koma],
                     [uma_suji, uma_dan - 1, koma]]
        for x in nari_list:
            no_ten = 6 not in x
            no_zero = 0 not in x

            if no_ten and no_zero:
                valid_list.append(x)

        return valid_list

    def movelist_RYU(self, sengo, suji, dan, koma, sente_list, gote_list):
        valid_list = []
        ryu_suji = suji
        ryu_dan = dan
        while (1 <= ryu_suji <= 5) and (1 <= ryu_dan <= 5):
            if sengo == 0:
                if ryu_suji == 1:
                    break
                if [ryu_suji - 1, ryu_dan] in sente_list:
                    break
                elif [ryu_suji - 1, ryu_dan] in gote_list:
                    valid_list.append([ryu_suji - 1, ryu_dan, koma])
                    break
                else:
                    valid_list.append([ryu_suji - 1, ryu_dan, koma])
            if sengo == 1:
                if [ryu_suji - 1, ryu_dan] in sente_list:
                    valid_list.append([ryu_suji - 1, ryu_dan, koma])
                    break
                elif [ryu_suji - 1, ryu_dan] in gote_list:
                    break
                else:
                    valid_list.append([ryu_suji - 1, ryu_dan, koma])

            ryu_suji = ryu_suji - 1
        ryu_suji = suji
        ryu_dan = dan
        while (1 <= ryu_suji <= 5) and (1 <= ryu_dan <= 5):
            if ryu_dan == 1:
                break
            if sengo == 0:
                if [ryu_suji, ryu_dan - 1] in sente_list:
                    break
                elif [ryu_suji, ryu_dan - 1] in gote_list:
                    valid_list.append([ryu_suji, ryu_dan - 1, koma])
                    break
                else:
                    valid_list.append([ryu_suji, ryu_dan - 1, koma])
            if sengo == 1:
                if [ryu_suji, ryu_dan - 1] in sente_list:
                    valid_list.append([ryu_suji, ryu_dan - 1, koma])
                    break
                elif [ryu_suji, ryu_dan - 1] in gote_list:
                    break
                else:
                    valid_list.append([ryu_suji, ryu_dan - 1, koma])

            ryu_suji = ryu_suji - 1
        ryu_suji = suji
        ryu_dan = dan
        while (1 <= ryu_suji <= 5) and (1 <= ryu_dan <= 5):
            if ryu_suji == 5:
                break
            if sengo == 0:
                if [ryu_suji + 1, ryu_dan] in sente_list:
                    break
                elif [ryu_suji + 1, ryu_dan] in gote_list:
                    valid_list.append([ryu_suji + 1, ryu_dan, koma])
                    break
                else:
                    valid_list.append([ryu_suji + 1, ryu_dan, koma])
            if sengo == 1:
                if [ryu_suji + 1, ryu_dan] in sente_list:
                    valid_list.append([ryu_suji + 1, ryu_dan, koma])
                    break
                elif [ryu_suji + 1, ryu_dan] in gote_list:
                    break
                else:
                    valid_list.append([ryu_suji + 1, ryu_dan, koma])

            ryu_suji = ryu_suji + 1
        ryu_suji = suji
        ryu_dan = dan
        while (1 <= ryu_suji <= 5) and (1 <= ryu_dan <= 5):
            if ryu_dan == 5:
                break
            if sengo == 0:
                if [ryu_suji, ryu_dan + 1] in sente_list:
                    break
                elif [ryu_suji, ryu_dan + 1] in gote_list:
                    valid_list.append([ryu_suji, ryu_dan + 1, koma])
                    break
                else:
                    valid_list.append([ryu_suji, ryu_dan + 1, koma])
            if sengo == 1:
                if [ryu_suji, ryu_dan + 1] in sente_list:
                    valid_list.append([ryu_suji, ryu_dan + 1, koma])
                    break
                elif [ryu_suji, ryu_dan + 1] in gote_list:
                    break
                else:
                    valid_list.append([ryu_suji, ryu_dan + 1, koma])

            ryu_suji = ryu_suji + 1
        nari_list = [[suji + 1, dan + 1, koma], [suji + 1, dan - 1, koma], [suji - 1, dan + 1, koma],
                     [suji - 1, dan - 1, koma]]
        for x in nari_list:
            no_ten = 6 not in x
            no_zero = 0 not in x

            if no_ten and no_zero:
                valid_list.append(x)

        return valid_list
