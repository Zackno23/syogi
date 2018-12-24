import requests


def gikou():
    sfen = "lnsgkgsnl/7b1/ppppppppp/9/9/9/P2PPPPPP/1B5R1/LNSGKGSNL b R2p 1"
    r = requests.get(
        url=f'https://17xn1ovxga.execute-api.ap-northeast-1.amazonaws.com/production/gikou?byoyomi=10000&position=sfen {sfen}')
    data = r.json()
    gikou_result = data['bestmove']
    print(gikou_result)



gikou()
