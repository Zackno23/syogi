import os
import random
import time

import pygame
import speech_recognition as sr
from mutagen.mp3 import MP3 as mp3

from hisya_kyo_kaku_extralist import Extralist
from movement_check import Judgement
from nari import get_narigoma, narigoma

#   初形
dan0 = [[1, '香'], [1, '桂'], [1, '銀'], [1, '金'], [1, "玉"], [1, '金'], [1, '銀'], [1, '桂'], [1, '香']]
dan1 = [[2, '＊'], [1, '飛'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [1, '角'], [2, '＊']]
dan2 = [[1, '歩'], [1, '歩'], [1, '歩'], [1, '歩'], [1, '歩'], [1, '歩'], [1, '歩'], [1, '歩'], [1, '歩']]
dan3 = [[2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊']]
dan4 = [[2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊']]
dan5 = [[2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊']]
dan6 = [[0, '歩'], [0, '歩'], [0, '歩'], [0, '歩'], [0, '歩'], [0, '歩'], [0, '歩'], [0, '歩'], [0, '歩']]
dan7 = [[2, '＊'], [0, '角'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [0, '飛'], [2, '＊']]
dan8 = [[0, '香'], [0, '桂'], [0, '銀'], [0, '金'], [0, "玉"], [0, '金'], [0, '銀'], [0, '桂'], [0, '香']]

shogiban = [dan0, dan1, dan2, dan3, dan4, dan5, dan6, dan7, dan8]
mochigoma_opponent = []
mochigoma_me = []


# 駒音の再生
def playsound():
    filename = "japanese-chess-piece1.mp3"  # 再生したいmp3ファイル
    pygame.mixer.init()
    pygame.mixer.music.load(filename)  # 音源を読み込み
    mp3_length = mp3(filename).info.length  # 音源の長さ取得
    pygame.mixer.music.play(1)  # 再生開始。1の部分を変えるとn回再生(その場合は次の行の秒数も×nすること)
    time.sleep(mp3_length + 0.25)  # 再生開始後、音源の長さだけ待つ(0.25待つのは誤差解消)
    pygame.mixer.music.stop()  # 音源の長さ待ったら再生停止


# 盤面の表示
def display(board):
    if len(mochigoma_opponent) > 0:
        print("後手の持駒リスト", mochigoma_opponent)
    for dan in range(len(board)):
        for i in board[dan]:
            print(i[1], end="")
        print("")
    if len(mochigoma_me) > 0:
        print("先手の持駒リスト", mochigoma_me)
    print("")


# 駒を判別し、movement_checkから動けるところリストを引っ張ってくる
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


def main():
    turn = random.randint(0, 1)
    oute = False
    sente_piece_list = []
    gote_piece_list = []
    empty_piece_list = []
    gotegyoku = Judgement()
    gotegyoku_mawalist = gotegyoku.movelist_GYOKU(1, 5, 1, "玉")
    gotegyoku_address = [5, 1]
    sente_hisya_list = [[2, 8]]
    sente_kyo_list = [[1, 9], [9, 9]]
    sente_kaku_list = [[8, 8]]
    sente_ryu_list = []
    sente_uma_list = []
    for a in range(len(shogiban)):
        for b in range(len(shogiban[a])):
            if shogiban[a][b][0] == 0:
                sente_piece_list.append([9 - b, a + 1])
            elif shogiban[a][b][0] == 1:
                gote_piece_list.append([9 - b, a + 1])
            elif shogiban[a][b][0] == 2:
                empty_piece_list.append([9 - b, a + 1])
    while True:

        if turn == 0:
            # 持ち駒があった場合の処理
            if len(mochigoma_me) > 0:
                question_drop = input("持ち駒を使いますか?(y/n)")
                if question_drop.lower() == 'y':
                    drop = input('どの駒を使いますか?')
                    print("移動先")
                    goal_Suji = int(input("筋"))
                    goal_Dan = int(input("段"))
                    if shogiban[goal_Dan - 1][9 - goal_Suji] != [2, "＊"]:
                        print("不正な指し手です")
                        os.system("say '不正な指し手です'")
                        continue

                    if drop not in mochigoma_me:
                        print("不正な指し手です")
                        os.system("say '不正な指し手です'")
                        continue

                    sente_piece_list.append([goal_Suji, goal_Dan])
                    empty_piece_list.remove([goal_Suji, goal_Dan])
                    shogiban[goal_Dan - 1][9 - goal_Suji] = [turn, drop]
                    num = mochigoma_me.index(drop)
                    mochigoma_me.pop(num)
                    if drop == "香":
                        sente_kyo_list.append([goal_Suji, goal_Dan])
                    elif drop == "飛":
                        sente_hisya_list.append([goal_Suji, goal_Dan])
                    elif drop == "角":
                        sente_kaku_list.append([goal_Suji, goal_Dan])
                    elif drop == "龍":
                        sente_ryu_list.append([goal_Suji, goal_Dan])
                    elif drop == "馬":
                        sente_uma_list.append([goal_Suji, goal_Dan])
                    # mawalistに指した駒の動ける範囲リストがかぶっていたらそれをリスト化
                    sashite_movement_lists = pieces(0, goal_Suji, goal_Dan, drop, sente_piece_list, gote_piece_list)
                    for sashite_movement in sashite_movement_lists:
                        if [sashite_movement[0], sashite_movement[1], "玉"] in gotegyoku_mawalist:
                            gotegyoku_mawalist.remove([sashite_movement[0], sashite_movement[1]])
                    if [gotegyoku_address[0], gotegyoku_address[1], drop] in sashite_movement_lists:
                        oute = True
                    turn = 1
                    playsound()
                    display(shogiban)

                    continue
            # 指し手の処理
            Origin_Suji = int(input("筋"))
            if Origin_Suji <= 0 or Origin_Suji >= 10:
                print("不正な指し手です。")
                os.system("say '不正な指し手です'")
            Origin_Dan = int(input("段"))
            if Origin_Dan <= 0 or Origin_Dan >= 10:
                print("不正な指し手です")
                os.system("say '不正な指し手です'")
            koma = shogiban[Origin_Dan - 1][9 - Origin_Suji]

            if shogiban[Origin_Dan - 1][9 - Origin_Suji][0] == turn:
                print("移動先")
                goal_Suji = int(input("筋"))
                goal_Dan = int(input("段"))
                moved = shogiban[goal_Dan - 1][9 - goal_Suji]
                if [goal_Suji, goal_Dan, koma[1]] not in pieces(turn,
                                                                Origin_Suji,
                                                                Origin_Dan, koma[1],
                                                                sente_piece_list,
                                                                gote_piece_list):
                    print("不正な指し手です。")
                    os.system("say '不正な指し手です'")
                    continue

                elif moved[0] != turn and moved[0] != 2:
                    moved = shogiban[goal_Dan - 1][9 - goal_Suji]
                    moved[0] = turn
                    if moved[1] == "玉":
                        os.system("say '負けました'")
                        break

                    if moved[1] == 'と' or moved[1] == '杏' or moved[1] == '圭' or moved[1] == '全' or moved[
                        1] == '龍' or \
                            moved[1] == '馬':
                        moved[1] = get_narigoma(moved[1])
                    mochigoma_me.append(moved[1])
                    gote_piece_list.remove([goal_Suji, goal_Dan])

                elif moved[0] == turn:
                    print("不正な指し手です。")
                    os.system("say '不正な指し手です'")
                    continue
                if (koma[1] == '歩' or koma[1] == '香' or koma[1] == '桂' or koma[1] == '銀' or koma[1] == '飛' or koma[
                    1] == '角'):
                    if goal_Dan <= 3:
                        narunaranai = input("成りますか?(y/n)")
                        if narunaranai.lower() == 'y':
                            koma[1] = narigoma(koma[1])
                            if koma[1] == "龍":
                                sente_hisya_list.remove([Origin_Suji, Origin_Dan])
                                sente_ryu_list.append([goal_Suji, goal_Dan])
                            if koma[1] == "馬":
                                sente_kaku_list.remove([Origin_Suji, Origin_Dan])
                                sente_uma_list.append([goal_Suji, goal_Dan])
                            if koma[1] == "杏":
                                sente_kyo_list.remove([Origin_Suji, Origin_Dan])
                sente_piece_list.append([goal_Suji, goal_Dan])
                sente_piece_list.remove([Origin_Suji, Origin_Dan])
                if moved[0] == 2:
                    empty_piece_list.remove([goal_Suji, goal_Dan])
                empty_piece_list.append([Origin_Suji, Origin_Dan])
                shogiban[Origin_Dan - 1][9 - Origin_Suji] = [2, '＊']
                shogiban[goal_Dan - 1][9 - goal_Suji] = koma
                motokoma = koma
                sashite_movement_lists = pieces(0, goal_Suji, goal_Dan, koma[1], sente_piece_list, gote_piece_list)

                if koma[1] == "飛":
                    sente_hisya_list.remove([Origin_Suji, Origin_Dan])
                    sente_hisya_list.append([goal_Suji, goal_Dan])
                if koma[1] == "角":
                    sente_kaku_list.remove([Origin_Suji, Origin_Dan])
                    sente_kaku_list.append([goal_Suji, goal_Dan])
                if koma[1] == "香":
                    sente_hisya_list.remove([Origin_Suji, Origin_Dan])
                    sente_hisya_list.append([goal_Suji, goal_Dan])
                if koma[1] == "龍" and motokoma == "龍":
                    sente_ryu_list.remove([Origin_Suji, Origin_Dan])
                    sente_ryu_list.append([goal_Suji, goal_Dan])
                if koma[1] == "馬" and motokoma == "馬":
                    sente_uma_list.remove([Origin_Suji, Origin_Dan])
                    sente_uma_list.append([goal_Suji, goal_Dan])

                extra = Extralist()
                gote_piece_list.remove(gotegyoku_address)
                for hisya in sente_hisya_list:
                    if len(extra.movelist_HISYA(0, hisya[0], hisya[1], '飛', sente_piece_list, gote_piece_list)) == 0:
                        pass
                    else:
                        for extras in extra.movelist_HISYA(0, hisya[0], hisya[1], '飛', sente_piece_list,
                                                           gote_piece_list):
                            sashite_movement_lists.append(extras)
                for kaku in sente_kaku_list:
                    if len(extra.movelist_KAKU(0, kaku[0], kaku[1], '角', sente_piece_list, gote_piece_list)) == 0:
                        pass
                    else:
                        for extras in extra.movelist_KAKU(0, kaku[0], kaku[1], '飛', sente_piece_list, gote_piece_list):
                            sashite_movement_lists.append(extras)
                for kyo in sente_kyo_list:
                    if len(extra.kyo_extralist(0, kyo[0], kyo[1], '香', sente_piece_list, gote_piece_list)) == 0:
                        pass
                    else:
                        for extras in extra.kyo_extralist(0, kyo[0], kyo[1], '香', sente_piece_list, gote_piece_list):
                            sashite_movement_lists.append(extras)

                for ryu in sente_ryu_list:
                    if len(extra.movelist_RYU(0, ryu[0], ryu[1], '龍', sente_piece_list, gote_piece_list)) == 0:
                        pass
                    else:
                        for extras in extra.movelist_RYU(0, ryu[0], ryu[1], '龍', sente_piece_list, gote_piece_list):
                            sashite_movement_lists.append(extras)
                for uma in sente_uma_list:
                    if len(extra.movelist_UMA(0, uma[0], uma[1], '馬', sente_piece_list, gote_piece_list)) == 0:
                        pass
                    for extras in extra.movelist_UMA(0, uma[0], uma[1], '馬', sente_piece_list, gote_piece_list):
                        sashite_movement_lists.append(extras)

                for sashite_movement in sashite_movement_lists:

                    if [sashite_movement[0], sashite_movement[1], "玉"] in gotegyoku_mawalist:
                        gotegyoku_mawalist.remove([sashite_movement[0], sashite_movement[1], "玉"])
                if [gotegyoku_address[0], gotegyoku_address[1], koma[1]] in sashite_movement_lists:
                    oute = True
                turn = 1

            else:
                print("不正な指し手です。")
                os.system("say '不正な指し手です'")

                continue
            gote_piece_list.append(gotegyoku_address)
            display(shogiban)
            playsound()

        elif turn == 1:
            if oute == True:
                if len(gotegyoku_mawalist) == 0:
                    print(pieces(1, gotegyoku_address[0], gotegyoku_address[1], '玉',
                                 sente_piece_list, gote_piece_list))
                    if [goal_Suji, goal_Dan, "玉"] in pieces(1, gotegyoku_address[0], gotegyoku_address[1], '玉',
                                                            sente_piece_list, gote_piece_list):
                        shogiban[goal_Dan - 1][9 - goal_Suji] = [1, "玉"]
                        shogiban[gotegyoku_address[1] - 1][9 - gotegyoku_address[0]] = [2, "＊"]
                        mochigoma_opponent.append(koma[1])
                        gotegyoku_address = [goal_Suji, goal_Dan]
                        gote_piece_list.append(gotegyoku_address)
                        display(shogiban)
                        playsound()
                        turn = 0
                        continue
                    else:
                        os.system("say '負けました'")
                        break
                gyoku_move = random.choice(gotegyoku_mawalist)

                moved = shogiban[gyoku_move[1] - 1][9 - gyoku_move[0]]
                if moved[0] == 1:
                    gotegyoku_mawalist.remove(gyoku_move)
                    continue
                # 玉が駒を取ったときの処理
                # print(moved)
                if moved[0] == 0:
                    mochigoma_opponent.append(moved[1])
                    if moved[1] == "香":
                        sente_kyo_list.remove([gyoku_move[0], gyoku_move[1]])
                    elif moved[1] == "飛":
                        sente_hisya_list.remove([gyoku_move[0], gyoku_move[1]])
                    elif moved[1] == "角":
                        sente_kaku_list.remove([gyoku_move[0], gyoku_move[1]])
                    elif moved[1] == "龍":
                        sente_ryu_list.remove([gyoku_move[0], gyoku_move[1]])
                    elif moved[1] == "馬":
                        sente_uma_list.remove([gyoku_move[0], gyoku_move[1]])
                    sente_piece_list.remove([gyoku_move[0], gyoku_move[1]])
                gote_piece_list.remove([gotegyoku_address[0], gotegyoku_address[1]])
                gote_piece_list.append([gyoku_move[0], gyoku_move[1]])
                if moved[0] == 2:
                    empty_piece_list.remove([gyoku_move[0], gyoku_move[1]])
                empty_piece_list.append([gotegyoku_address[0], gotegyoku_address[1]])

                shogiban[gotegyoku_address[1] - 1][9 - gotegyoku_address[0]] = [2, '＊']
                shogiban[gyoku_move[1] - 1][9 - gyoku_move[0]] = [1, "玉"]
                turn = 0
                display(shogiban)
                playsound()
                gotegyoku_address = [gyoku_move[0], gyoku_move[1]]
                gotegyoku = Judgement()
                gotegyoku_mawalist = gotegyoku.movelist_GYOKU(1, gotegyoku_address[0], gotegyoku_address[1], "玉")
                ugokeru_list = []
                for piece in sente_piece_list:
                    ugokeru_list.append(
                        pieces(0, piece[0], piece[1], shogiban[piece[1] - 1][9 - piece[0]][1], sente_piece_list,
                               gote_piece_list))
                for a in ugokeru_list:
                    for b in a:
                        if [b[0], b[1], "玉"] in gotegyoku_mawalist:
                            gotegyoku_mawalist.remove([b[0], b[1], "玉"])

                oute = False

            else:
                # time.sleep(random.randint(5, 10))
                if len(mochigoma_opponent) != 0:
                    gote_piece_list.append(mochigoma_opponent)
                gote_choice = random.choice(gote_piece_list)
                if gote_choice == mochigoma_opponent:
                    gote_drop_piece = random.choice(mochigoma_opponent)
                    gote_drop_place = random.choice(empty_piece_list)
                    shogiban[gote_drop_place[1] - 1][9 - gote_drop_place[0]] = [turn, gote_drop_piece]
                    num = mochigoma_opponent.index(gote_drop_piece)
                    mochigoma_opponent.pop(num)
                    gote_piece_list.append(gote_drop_place)
                    empty_piece_list.remove(gote_drop_place)

                else:
                    chozen_koma = shogiban[gote_choice[1] - 1][9 - gote_choice[0]]

                    if len(pieces(turn, gote_choice[0], gote_choice[1], chozen_koma[1], sente_piece_list,
                                  gote_piece_list)) == 0:
                        continue
                    gote_move = random.choice(
                        pieces(turn, gote_choice[0], gote_choice[1], chozen_koma[1], sente_piece_list, gote_piece_list))
                    moved = shogiban[gote_move[1] - 1][9 - gote_move[0]]
                    if moved[0] == 1:
                        continue
                    if moved[1] == "玉":
                        os.system("say 'お前の負けだ。十年早い'")
                        break
                    # 成り駒を取ったときの処理
                    if moved[0] != 2:
                        if moved[1] == 'と' or moved[1] == '杏' or moved[1] == '圭' or moved[1] == '全' or moved[
                            1] == '龍' or \
                                moved[1] == '馬':
                            moved[1] = get_narigoma(moved[1])
                        if moved[1] == "飛":
                            sente_hisya_list.remove([gote_move[0], gote_move[1]])
                        elif moved[1] == "角":
                            sente_kaku_list.remove([gote_move[0], gote_move[1]])
                        elif moved[1] == "香":
                            sente_kyo_list.remove([gote_move[0], gote_move[1]])
                        elif moved[1] == "龍":
                            sente_ryu_list.remove([gote_move[0], gote_move[1]])
                        elif moved[1] == "馬":
                            sente_uma_list.remove([gote_move[0], gote_move[1]])
                        mochigoma_opponent.append(moved[1])
                        sente_piece_list.remove([gote_move[0], gote_move[1]])

                    # 駒を成る処理
                    if (chozen_koma[1] == '歩' or chozen_koma[1] == '香' or chozen_koma[1] == '桂' or chozen_koma[
                        1] == '銀' or
                            chozen_koma[1] == '飛' or chozen_koma[
                                1] == '角'):
                        if gote_move[1] >= 7:
                            chozen_koma[1] = narigoma(chozen_koma[1])
                    # 駒の移動
                    gote_piece_list.remove([gote_choice[0], gote_choice[1]])
                    gote_piece_list.append([gote_move[0], gote_move[1]])
                    if moved[0] == 2:
                        empty_piece_list.remove([gote_move[0], gote_move[1]])
                    empty_piece_list.append([gote_choice[0], gote_choice[1]])

                    shogiban[gote_choice[1] - 1][9 - gote_choice[0]] = [2, '＊']
                    shogiban[gote_move[1] - 1][9 - gote_move[0]] = chozen_koma
                    turn = 0
                    display(shogiban)
                    playsound()
                    continue


if __name__ == "__main__":

    display(shogiban)

    # 「お願いします」
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    text = (r.recognize_google(audio, language='ja-JP'))
    if text == "お願いします":
        os.system("say 'お願いします。'")
    main()
