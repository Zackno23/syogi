import requests

from nari import get_narigoma, narigoma
from piece_selection import pieces
from syogiban2sfen import Syogiban2sfen

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

CPUの持ち駒 = ["歩", "香"]
プレーヤーの持ち駒 = []


def gikou(sfen):
    r = requests.get(
        url=f'https://17xn1ovxga.execute-api.ap-northeast-1.amazonaws.com/production/gikou?byoyomi=10000&position=sfen {sfen}')
    data = r.json()
    gikou_result = data['bestmove']
    return gikou_result


def display(board):
    if len(CPUの持ち駒) > 0:
        for i in CPUの持ち駒:
            print(i, end=" ")
        print("")
    for dan in range(len(board)):
        for i in board[dan]:
            print(i[1], end="")
        print("")
    if len(プレーヤーの持ち駒) > 0:
        for i in プレーヤーの持ち駒:
            print(i, end=" ")
        print("")


def kifu_to_baord(suji, dan, shogiban):  # 符号からshogibanのリスト表記に変換
    return shogiban[dan - 1][9 - suji]


def main():
    turn = 0
    while True:
        先手駒リスト = []
        後手駒リスト = []
        empty_piece_list = []
        for a in range(len(shogiban)):
            for b in range(len(shogiban[a])):
                if shogiban[a][b][0] == 0:
                    先手駒リスト.append([9 - b, a + 1])
                elif shogiban[a][b][0] == 1:
                    後手駒リスト.append([9 - b, a + 1])
                elif shogiban[a][b][0] == 2:
                    empty_piece_list.append([9 - b, a + 1])
        if turn == 0:
            # 持ち駒があったときの処理
            if len(プレーヤーの持ち駒) >= 1:
                question = input("持ち駒を使いますか(y/n)")
                if question.lower() == "y":
                    打ち駒 = input("どの駒を使いますか?")
                    if 打ち駒 in プレーヤーの持ち駒:
                        打ち筋 = int(input("筋:"))
                        打ち段 = int(input("段"))
                        if kifu_to_baord(打ち筋, 打ち段, shogiban)[0] == 2:
                            if 打ち駒 == "歩":
                                二歩 = False
                                for dan in shogiban:
                                    if dan[9 - 打ち筋] == [turn, "歩"]:
                                        二歩 = True
                                if 二歩:
                                    print("二歩です")
                                    continue
                            shogiban[打ち段 - 1][9 - 打ち筋] = [turn, 打ち駒]
                            プレーヤーの持ち駒.remove("打ち駒")
                            turn = 1
                            display(shogiban)
                            continue
                        else:
                            print("そこには打てません。")
                            continue
                    else:
                        print("駒を持っていません。")
                        continue

            # 駒を打たない場合の、さしての処理
            移動元_筋 = int(input("筋:"))
            移動元_段 = int(input("段:"))
            if kifu_to_baord(移動元_筋, 移動元_段, shogiban, )[0] != turn:
                print("不正なさしてです")
                continue
            動かす駒 = kifu_to_baord(移動元_筋, 移動元_段, shogiban, )[1]
            移動先_筋 = int(input("筋"))
            移動先_段 = int(input("段"))
            if kifu_to_baord(移動先_筋, 移動先_段, shogiban)[0] == turn:
                print("不正な指し手です。")
                continue
            elif [移動先_筋, 移動先_段, 動かす駒] not in pieces(turn, 移動元_筋, 移動元_段, 動かす駒, 先手駒リスト, 後手駒リスト):
                print(pieces(turn, 移動元_筋, 移動元_段, 動かす駒, 先手駒リスト, 後手駒リスト))
                print("不正な指し手です。")
                continue
            elif kifu_to_baord(移動先_筋, 移動先_段, shogiban)[0] == 1:
                取る駒 = kifu_to_baord(移動先_筋, 移動先_段, shogiban)[1]
                取る駒 = get_narigoma(取る駒)
                プレーヤーの持ち駒.append(取る駒)
            if 移動先_段 <= 3:
                if 動かす駒 == "歩" or 動かす駒 == "香" or 動かす駒 == "桂" or 動かす駒 == "銀" or 動かす駒 == "飛" or 動かす駒 == "角":
                    nari_question = input("成りますか?(y/n)")
                    if nari_question.lower() == "y":
                        動かす駒 = narigoma(動かす駒)
            shogiban[移動元_段 - 1][9 - 移動元_筋] = [2, "＊"]
            shogiban[移動先_段 - 1][9 - 移動先_筋] = [turn, 動かす駒]
            turn = 1
            display(shogiban)
            continue

        if turn == 1:
            banmen = Syogiban2sfen()
            sfen = banmen.sfen(shogiban, turn, プレーヤーの持ち駒, CPUの持ち駒)
            print(sfen)
            result = gikou(sfen)
            print(result)
            if result[1:2] == "*":

            if result[4:] == "+":

            # 二文字めが*だったら打ちなので、CPUの持ち駒から削除し、盤面を変更する
            # 移動先に駒があるかをチェックし、CPUの持ち駒に足し、盤面を変更
            # 最後の文字が+の場合は、駒の成り
            # 先手玉をとった場合、先手の負けの処理

            turn = 0
            continue


if __name__ == "__main__":
    display(shogiban)
    # 「お願いします」
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
