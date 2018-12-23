import requests


def gikou():
    sfen = "lnsg1gsnk/1r5b1/ppppppppP/pl7/9/9/PPPPPPPP8/1B5R1/LNS1KGSNL w - 1"
    r = requests.get(
        url=f'https://17xn1ovxga.execute-api.ap-northeast-1.amazonaws.com/production/gikou?byoyomi=10000&position=sfen {sfen}')
    data = r.json()
    # gikou_result = data['bestmove']
    # print(gikou_result)
    print(data)

gikou()
