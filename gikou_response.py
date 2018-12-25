import requests


def gikou():
    sfen = "lnsgkgsnl/7b1/ppppppppp/9/9/9/P2PPPPPP/1B5R1/LNSGKGSNL b R2p 1"
    r = requests.get(
        url=f'https://17xn1ovxga.execute-api.ap-northeast-1.amazonaws.com/production/gikou?byoyomi=10000&position=sfen {sfen}')
    data = r.json()
    gikou_result = data['bestmove']
    print(gikou_result)



gikou()

"""
駒を移動させる前に、移動先に駒があるかどうかチェックする必要がある。
    sente_piece_listを引数として与える必要がある。
    取った駒を返り血として返す必要がある

移動した駒が成るとき
    最後の一文字が+になる
持ち駒を打った場合
    二文字めが*になる

"""
