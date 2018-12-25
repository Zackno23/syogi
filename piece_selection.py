from movement_check import Judgement


def pieces(turn, suji, dan, koma, sente_list, gote_list):
    if koma == "歩":
        fu = Judgement()
        area = fu.movelist_FU(turn, suji, dan, koma)
        return area

    if koma == "香":
        kyo = Judgement()
        area = kyo.movelist_kyo(turn, suji, dan, koma, sente_list, gote_list)
        return area

    if koma == "桂":
        keima = Judgement()
        area = keima.movelist_kei(turn, suji, dan, koma)
        return area

    if koma == "銀":
        gin = Judgement()
        area = gin.movelist_gin(turn, suji, dan, koma)
        return area

    if koma == "金" or koma == 'と' or koma == '杏' or koma == '圭' or koma == '全':
        kin = Judgement()
        area = kin.movelist_kin(turn, suji, dan, koma)
        return area

    if koma == "飛":
        hisya = Judgement()
        area = hisya.movelist_HISYA(turn, suji, dan, koma, sente_list, gote_list)
        return area

    if koma == "角":
        kaku = Judgement()
        area = kaku.movelist_KAKU(turn, suji, dan, koma, sente_list, gote_list)
        return area

    if koma == "玉":
        gyoku = Judgement()
        area = gyoku.movelist_GYOKU(turn, suji, dan, koma)
        return area

    if koma == "馬":
        uma = Judgement()
        area = uma.movelist_UMA(turn, suji, dan, koma, sente_list, gote_list)
        return area

    if koma == "龍":
        ryu = Judgement()
        area = ryu.movelist_RYU(turn, suji, dan, koma, sente_list, gote_list)
        return area
