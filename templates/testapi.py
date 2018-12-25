import requests


def gikou(sfen):
    r = requests.get(
        url=f'https://17xn1ovxga.execute-api.ap-northeast-1.amazonaws.com/production/gikou?byoyomi=10000&position=sfen{sfen}')
    data = r.json()
    gikou_result = data['bestmove']
    print(gikou_result)
    print(data)


gikou("%20lnsgkgsnl/1r5b1/pppppp%2bRpp/9/9/2P6/PP1PPPPPP/7R1/LNSGKGSNL%20w%20P%201")
