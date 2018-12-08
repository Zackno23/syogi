class Extralist:
    def kyo_extralist(self, sengo, suji, dan, koma, sente_list, gote_list, gyoku_address):
        valid_list = []
        if sengo == 0:
            if dan != 1:
                for i in range(dan - 1):
                    if [suji, 8 - i] in sente_list:
                        break
                    elif [suji, 8 - 1] in gote_list:
                        valid_list.append([suji, 8 - i, koma])
                        break
                    else:
                        valid_list.append([suji, 8 - i, koma])
            else:
                return []
        elif sengo == 1:
            if dan != 9:
                for i in range(8 - dan):
                    if [suji, dan + 1 + i] in sente_list:
                        valid_list.append([[suji, dan + 1 + i], koma])
                    elif [suji, dan + 1 + i] in gote_list:
                        break
                    else:
                        valid_list.append([suji, dan + 1 + i, koma])
            else:
                return []
        return valid_list

    def movelist_KAKU(self, sengo, suji, dan, koma, sente_list, gote_list, gyoku_address):
        valid_list = []
        kaku_suji = suji
        kaku_dan = dan
        while (1 <= kaku_suji <= 9) and (1 <= kaku_dan <= 9):
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

        while (1 <= kaku_suji <= 9) and (1 <= kaku_dan <= 9):
            if kaku_suji == 9 or kaku_dan == 1:
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
        while (1 <= kaku_suji <= 9) and (1 <= kaku_dan <= 9):
            if kaku_suji == 9 or kaku_dan == 9:
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
        while (1 <= kaku_suji <= 9) and (1 <= kaku_dan <= 9):
            if kaku_suji == 1 or kaku_dan == 9:
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

    def movelist_HISYA(self, sengo, suji, dan, koma, sente_list, gote_list, gyoku_address):
        valid_list = []
        hisya_suji = suji
        hisya_dan = dan

        while (1 <= hisya_suji <= 9) and (1 <= hisya_dan <= 9):
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

        while (1 <= hisya_suji <= 9) and (1 <= hisya_dan <= 9):
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
        while (1 <= hisya_suji <= 9) and (1 <= hisya_dan <= 9):
            if hisya_suji == 9:
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
        while (1 <= hisya_suji <= 9) and (1 <= hisya_dan <= 9):
            if hisya_dan == 9:
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

            hisya_dan = hisya_dan + 1
        return valid_list

    def movelist_UMA(self, sengo, suji, dan, koma, sente_list, gote_list, gyoku_address):
        valid_list = []
        uma_suji = suji
        uma_dan = dan
        while (1 <= uma_suji <= 9) and (1 <= uma_dan <= 9):
            if uma_suji == 1 or uma_dan == 9:
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

        while (1 <= uma_suji <= 9) and (1 <= uma_dan <= 9):
            if uma_suji == 9 or uma_suji == 1:
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
        while (1 <= uma_suji <= 9) and (1 <= uma_dan <= 9):
            if uma_suji == 9 or uma_dan == 9:
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
        while (1 <= uma_suji <= 9) and (1 <= uma_dan <= 9):
            if uma_suji == 1 or uma_dan == 9:
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

    def movelist_RYU(self, sengo, suji, dan, koma, sente_list, gote_list, gyoku_address):
        valid_list = []
        ryu_suji = suji
        ryu_dan = dan
        while (1 <= ryu_suji <= 9) and (1 <= ryu_dan <= 9):
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
        while (1 <= ryu_suji <= 9) and (1 <= ryu_dan <= 9):
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

            ryu_dan = ryu_dan - 1
        ryu_suji = suji
        ryu_dan = dan
        while (1 <= ryu_suji <= 9) and (1 <= ryu_dan <= 9):
            if ryu_suji == 9:
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
        while (1 <= ryu_suji <= 9) and (1 <= ryu_dan <= 9):
            if ryu_dan == 9:
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

            ryu_dan = ryu_dan + 1
        nari_list = [[suji + 1, dan + 1, koma], [suji + 1, dan - 1, koma], [suji - 1, dan + 1, koma],
                     [suji - 1, dan - 1, koma]]
        for x in nari_list:
            no_ten = 6 not in x
            no_zero = 0 not in x

            if no_ten and no_zero:
                valid_list.append(x)

        return valid_list
