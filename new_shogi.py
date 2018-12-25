dan0 = [[1, '香'], [1, '桂'], [1, '銀'], [1, '金'], [1, "玉"], [1, '金'], [1, '銀'], [1, '桂'], [1, '香']]
dan1 = [[2, '＊'], [1, '飛'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [1, '角'], [2, '＊']]
dan2 = [[1, '歩'], [1, '歩'], [1, '歩'], [1, '歩'], [1, '歩'], [1, '歩'], [1, '歩'], [1, '歩'], [1, '歩']]
dan3 = [[2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊']]
dan4 = [[2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊']]
dan5 = [[2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊']]
dan6 = [[0, '歩'], [2, '＊'], [0, '歩'], [0, '歩'], [0, '歩'], [0, '歩'], [0, '歩'], [0, '歩'], [0, '歩']]
dan7 = [[2, '＊'], [0, '角'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [2, '＊'], [0, '飛'], [2, '＊']]
dan8 = [[0, '香'], [0, '桂'], [0, '銀'], [0, '金'], [0, "玉"], [0, '金'], [0, '銀'], [0, '桂'], [0, '香']]
shogiban = [dan0, dan1, dan2, dan3, dan4, dan5, dan6, dan7, dan8]

CPUの持ち駒 = []
プレーヤーの持ち駒 = ["歩"]


def display(board):
    if len(CPUの持ち駒) > 0:
        for i in CPUの持ち駒:
            print(i)
    for dan in range(len(board)):
        for i in board[dan]:
            print(i[1], end="")
        print("")
    if len(プレーヤーの持ち駒) > 0:
        for i in プレーヤーの持ち駒:
            print(i)


def kifu_to_baord(suji, dan, shogiban):
    return shogiban[dan - 1][9 - suji]


def main():
    turn = 0
    while True:
        if turn == 0:
            while len(プレーヤーの持ち駒) >= 1:
                question = input("持ち駒を使いますか(y/n)")
                if question.lower() == "n":
                    break
                if question.lower() == "y":
                    打ち駒 = input("どの駒を使いますか?")
                    if 打ち駒 in プレーヤーの持ち駒:
                        打ち筋 = int(input("筋:"))
                        打ち段 = int(input("段"))
                        if kifu_to_baord(打ち筋, 打ち段, shogiban)[0] == 2:
                            if 打ち駒 == "歩":
                                for dan in shogiban:
                                    if dan[9 - 打ち筋] == [turn, "歩"]:
                                        二歩 = True
                                if 二歩:
                                    print("二歩です")
                                    continue
                            shogiban[打ち段 - 1][9 - 打ち筋] = [turn, 打ち駒]
                            turn = 1
                            display(shogiban)
                            break
                        else:
                            print("そこには打てません。")
                            continue
                    else:
                        print("駒を持っていません。")
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
