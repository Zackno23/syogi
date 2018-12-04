import os
import time

import pygame
from mutagen.mp3 import MP3 as mp3

from movement_check import Judgement

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

# 初形の表示
def display(board):
    for dan in range(len(board)):
        for i in board[dan]:
            print(i[1], end="")
        print("")


# 駒を判別し、movement_checkから動けるところリストを引っ張ってくる
def pieces(turn, suji, dan, koma):
    if koma == "歩":
        fu = Judgement()
        area = fu.movelist_FU(turn, suji, dan, koma)

        return area

    if koma == "香":
        return Judgement.movelist_kyo(turn, suji, dan, koma)

    if koma == "桂":
        return Judgement.movelist_kei(turn, suji, dan, koma)

    if koma == "銀":
        return Judgement.movelist_gin(turn, suji, dan, koma)

    if koma == "金":
        return Judgement.movelist_kin(turn, suji, dan, koma)

    if koma == "飛":
        return Judgement.movelist_HISYA(turn, suji, dan, koma)

    if koma == "角":
        kaku = Judgement()
        area = kaku.movelist_KAKU(turn, suji, dan, koma)
        return area


    if koma == "玉":
        return Judgement.movelist_GYOKU(turn, suji, dan, koma)


def main():
    turn = 0
    while True:
        # 持ち駒があった場合の処理
        if (turn == 0 and len(mochigoma_me) > 0) or (turn == 1 and len(mochigoma_opponent) > 0):
            question_drop = input("持ち駒を使いますか?(y/n)")
            if question_drop.lower() == 'y':
                drop = input('どの駒を使いますか?')
                print("移動先")
                goal_Suji = int(input("筋"))
                goal_Dan = int(input("段"))
                if shogiban[goal_Dan - 1][9 - goal_Suji] != [2, "＊"]:
                    print("不正な指し手です")
                    os.system("say '不正な指し手です'")
                shogiban[goal_Dan - 1][9 - goal_Suji] = [0, drop]
                if turn == 0:
                    num = mochigoma_me.index([0, drop])
                    mochigoma_me.pop(num)
                elif turn == 1:
                    num = mochigoma_opponent.index([0, drop])
                    mochigoma_opponent.pop(num)

                if turn == 0:
                    turn = 1
                elif turn == 1:
                    turn = 0
                playsound()
                print(mochigoma_opponent)
                display(shogiban)
                print(mochigoma_me)
                continue
        # 指し手の処理
        Origin_Suji = int(input("筋"))
        Origin_Dan = int(input("段"))
        koma = shogiban[Origin_Dan - 1][9 - Origin_Suji]

        if shogiban[Origin_Dan - 1][9 - Origin_Suji][0] == turn:
            print("移動先")
            goal_Suji = int(input("筋"))
            goal_Dan = int(input("段"))

            print(pieces(turn, Origin_Suji, Origin_Dan, koma[1]))
            if [goal_Suji, goal_Dan, koma[1]] not in pieces(turn, Origin_Suji, Origin_Dan, koma[1]):
                print("不正な指し手です。")
                #os.system("say '不正な指し手です'")

            moved = shogiban[goal_Dan - 1][9 - goal_Suji]

            if moved[0] != turn and moved[0] != 2:
                moved[0] = turn
                if moved[1] == "玉":
                    os.system("say '負けました'")
                    break
                if turn == 0:
                    mochigoma_me.append(moved)
                else:
                    mochigoma_opponent.append(moved)

            shogiban[Origin_Dan - 1][9 - Origin_Suji] = [2, '＊']
            shogiban[goal_Dan - 1][9 - goal_Suji] = koma

            playsound()
            if turn == 0:
                turn = 1
            elif turn == 1:
                turn = 0
        else:
            print("不正な指し手です。")
            os.system("say '不正な指し手です'")

            continue

        print(mochigoma_opponent)
        display(shogiban)
        print(mochigoma_me)


if __name__ == "__main__":
    display(shogiban)
    # r = sr.Recognizer()
    # mic = sr.Microphone()
    #
    # with mic as source:
    #     r.adjust_for_ambient_noise(source)
    #     audio = r.listen(source)
    # text = (r.recognize_google(audio, language='ja-JP'))
    # if text == 'お願いします':
    #     os.system("say 'お願いします。'")
    main()
