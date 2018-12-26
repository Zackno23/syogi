def sfen2sashite(sfen):
    if sfen == "p":
        return "歩"
    if sfen == "l":
        return "香"
    if sfen == "n":
        return "桂"
    if sfen == "s":
        return "銀"
    if sfen == "g":
        return "金"
    if sfen == "r":
        return "飛"
    if sfen == "b":
        return '角'


def dan_sfen2banmen(dan):
    if dan == "a":
        return 1
    if dan == "b":
        return 2
    if dan == "c":
        return 3
    if dan == "d":
        return 4
    if dan == "e":
        return 5
    if dan == "f":
        return 6
    if dan == "g":
        return 7
    if dan == "h":
        return 8
    if dan == "i":
        return 9
