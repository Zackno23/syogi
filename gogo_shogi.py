import os
import random
import time

import pygame
from mutagen.mp3 import MP3 as mp3

from movement_check_GOGO import Judgement_gogo
from nari import get_narigoma, narigoma

dan0 = [[1, '飛'], [1, '角'], [1, '銀'], [1, '金'], [1, "玉"]]
dan1 = [[2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [1, '歩']]
dan2 = [[2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊']]
dan3 = [[0, '歩'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊']]
dan4 = [[0, '玉'], [0, '金'], [0, '銀'], [0, '角'], [0, '飛']]

shogiban = [dan0, dan1, dan2, dan3, dan4]
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
        print(mochigoma_opponent)
    for dan in range(len(board)):
        for i in board[dan]:
            print(i[1], end="")
        print("")
    if len(mochigoma_me) > 0:
        print(mochigoma_me)
    print("")


# 駒を判別し、movement_checkから動けるところリストを引っ張ってくる
def pieces(turn, suji, dan, koma, sente_list, gote_list):
    if koma == "歩":
        fu = Judgement_gogo()
        area = fu.movelist_FU(turn, suji, dan, koma)
        return area

    if koma == "香":
        kyo = Judgement_gogo()
        area = kyo.movelist_kyo(turn, suji, dan, koma, sente_list, gote_list)
        return area

    if koma == "桂":
        keima = Judgement_gogo()
        area = keima.movelist_kei(turn, suji, dan, koma)
        return area

    if koma == "銀":
        gin = Judgement_gogo()
        area = gin.movelist_gin(turn, suji, dan, koma)
        return area

    if koma == "金" or koma == 'と' or koma == '杏' or koma == '圭' or koma == '全':
        kin = Judgement_gogo()
        area = kin.movelist_kin(turn, suji, dan, koma)
        return area

    if koma == "飛":
        hisya = Judgement_gogo()
        area = hisya.movelist_HISYA(turn, suji, dan, koma, sente_list, gote_list)
        return area

    if koma == "角":
        kaku = Judgement_gogo()
        area = kaku.movelist_KAKU(turn, suji, dan, koma, sente_list, gote_list)
        return area

    if koma == "玉":
        gyoku = Judgement_gogo()
        area = gyoku.movelist_GYOKU(turn, suji, dan, koma)
        return area

    if koma == "馬":
        uma = Judgement_gogo()
        area = uma.movelist_UMA(turn, suji, dan, koma, sente_list, gote_list)
        return area

    if koma == "龍":
        ryu = Judgement_gogo()
        area = ryu.movelist_RYU(turn, suji, dan, koma, sente_list, gote_list)
        return area


def main():
    turn = 0
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
                    if shogiban[goal_Dan - 1][5 - goal_Suji] != [2, "＊"]:
                        print("不正な指し手ですよ")
                        os.system("say '不正な指し手です'")
                        continue

                    if drop not in mochigoma_me:
                        print("不正な指し手ですyo")
                        os.system("say '不正な指し手です'")
                        continue
                    sente_piece_list.append([goal_Suji, goal_Dan])
                    empty_piece_list.remove([goal_Suji, goal_Dan])
                    shogiban[goal_Dan - 1][5 - goal_Suji] = [turn, drop]
                    num = mochigoma_me.index(drop)
                    mochigoma_me.pop(num)

                    turn = 1
                    playsound()
                    display(shogiban)
                    continue
            # 指し手の処理
            Origin_Suji = int(input("筋"))
            if Origin_Suji <= 0 or Origin_Suji >= 6:
                print("不正な指し手です。")
                os.system("say '不正な指し手です'")
            Origin_Dan = int(input("段"))
            if Origin_Dan <= 0 or Origin_Dan >= 6:
                print("不正な指し手です")
                os.system("say '不正な指し手です'")
            koma = shogiban[Origin_Dan - 1][5 - Origin_Suji]

            if shogiban[Origin_Dan - 1][5 - Origin_Suji][0] == turn:
                print("移動先")
                goal_Suji = int(input("筋"))
                goal_Dan = int(input("段"))
                moved = shogiban[goal_Dan - 1][5 - goal_Suji]
                print(pieces(turn, Origin_Suji,
                             Origin_Dan, koma[1],
                             sente_piece_list,
                             gote_piece_list))
                if [goal_Suji, goal_Dan, koma[1]] not in pieces(turn, Origin_Suji,
                                                                Origin_Dan, koma[1],
                                                                sente_piece_list,
                                                                gote_piece_list):
                    print("不正な指し手ですが。")
                    os.system("say '不正な指し手です'")
                    continue

                elif moved[0] != turn and moved[0] != 2:
                    moved = shogiban[goal_Dan - 1][5 - goal_Suji]
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
                    print("不正な指し手ですし。")
                    os.system("say '不正な指し手です'")
                    continue
                if (koma[1] == '歩' or koma[1] == '香' or koma[1] == '桂' or koma[1] == '銀' or koma[1] == '飛' or koma[
                    1] == '角'):
                    if goal_Dan == 1:
                        narunaranai = input("成りますか?(y/n)")
                        if narunaranai.lower() == 'y':
                            koma[1] = narigoma(koma[1])
                sente_piece_list.append([goal_Suji, goal_Dan])
                sente_piece_list.remove([Origin_Suji, Origin_Dan])
                if moved[0] == 2:
                    empty_piece_list.remove([goal_Suji, goal_Dan])
                empty_piece_list.append([Origin_Suji, Origin_Dan])
                shogiban[Origin_Dan - 1][5 - Origin_Suji] = [2, '＊']
                shogiban[goal_Dan - 1][5 - goal_Suji] = koma
                turn = 1

            else:
                print("不正な指し手ですyo。")
                os.system("say '不正な指し手です'")

                continue

            display(shogiban)
            playsound()

        elif turn == 1:
            time.sleep(random.randint(5, 10))
            if len(mochigoma_opponent) != 0:
                gote_piece_list.append(mochigoma_opponent)
            gote_choice = random.choice(gote_piece_list)
            if gote_choice == mochigoma_opponent:
                gote_drop_piece = random.choice(mochigoma_opponent)
                gote_drop_place = random.choice(empty_piece_list)
                shogiban[gote_drop_place[1] - 1][5 - gote_drop_place[0]] = [turn, gote_drop_piece]
                num = mochigoma_opponent.index(gote_drop_piece)
                mochigoma_opponent.pop(num)
                gote_piece_list.append(gote_drop_place)
                empty_piece_list.remove(gote_drop_place)

            else:
                chozen_koma = shogiban[gote_choice[1] - 1][5 - gote_choice[0]]
                print(gote_choice)
                print(pieces(turn, gote_choice[0], gote_choice[1], chozen_koma[1], sente_piece_list, gote_piece_list))
                gote_move = random.choice(
                    pieces(turn, gote_choice[0], gote_choice[1], chozen_koma[1], sente_piece_list, gote_piece_list))
                moved = shogiban[gote_move[1] - 1][5 - gote_move[0]]
                if moved[0] == 1:
                    continue
                if moved[1] == "玉":
                    os.system("say 'お前の負けだ。十年早い'")
                    break
                # 成り駒を取ったときの処理
                if moved[0] != 2:
                    if moved[1] == 'と' or moved[1] == '杏' or moved[1] == '圭' or moved[1] == '全' or moved[1] == '龍' or \
                            moved[1] == '馬':
                        moved[1] = get_narigoma(moved[1])
                    mochigoma_opponent.append(moved[1])
                    sente_piece_list.remove([gote_move[0], gote_move[1]])

                # 駒を成る処理
                if (chozen_koma[1] == '歩' or chozen_koma[1] == '香' or chozen_koma[1] == '桂' or chozen_koma[1] == '銀' or
                        chozen_koma[1] == '飛' or chozen_koma[
                            1] == '角'):
                    if gote_move[1] == 5:
                        chozen_koma[1] = narigoma(chozen_koma[1])
                # 駒の移動
                gote_piece_list.remove([gote_choice[0], gote_choice[1]])
                gote_piece_list.append([gote_move[0], gote_move[1]])
                if moved[0] == 2:
                    empty_piece_list.remove([gote_move[0], gote_move[1]])
                empty_piece_list.append([gote_choice[0], gote_choice[1]])

                shogiban[gote_choice[1] - 1][5 - gote_choice[0]] = [2, '＊']
                shogiban[gote_move[1] - 1][5 - gote_move[0]] = chozen_koma
                turn = 0
                display(shogiban)
                playsound()
                continue


if __name__ == "__main__":
    #  先手の駒、後手の駒をそれぞれリストアップする。
    #  香車、飛車、角、竜王、馬のため
    #  自分の駒や相手の駒を飛び越したりしないため
    sente_piece_list = []
    gote_piece_list = []
    empty_piece_list = []
    for a in range(len(shogiban)):
        for b in range(len(shogiban[a])):
            if shogiban[a][b][0] == 0:
                sente_piece_list.append([5 - b, a + 1])
            elif shogiban[a][b][0] == 1:
                gote_piece_list.append([5 - b, a + 1])
            elif shogiban[a][b][0] == 2:
                empty_piece_list.append([5 - b, a + 1])
    display(shogiban)

    # r = sr.Recognizer()
    # mic = sr.Microphone()
    #
    # with mic as source:
    #     r.adjust_for_ambient_noise(source)
    #     audio = r.listen(source)
    # text = (r.recognize_google(audio, language='ja-JP'))
    # if text == "お願いします":
    #     os.system("say 'お願いします。'")
    main()
