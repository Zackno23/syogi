with open("onlyFu.csv") as ban:
    shogiban = ban.read().split("\n")
    print(shogiban)
cyakusyuA = int(input("筋"))  # 2
cyakusyuB = int(input("段"))  # 3

if shogiban[cyakusyuB - 1][3 - cyakusyuA] == "歩":  # 本番ではshogiban[cyakusyuB-1][9-cyakusyuA]
    new_dan = shogiban[2][:1] + "＊" + shogiban[2][2:]
    shogiban[2] = new_dan
    new_suji = shogiban[1][:1] + "歩" + shogiban[1][2:]
    shogiban[1] = new_suji
    print(shogiban)
