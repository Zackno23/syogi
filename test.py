import requests

r = requests.get(
    url='https://17xn1ovxga.execute-api.ap-northeast-1.amazonaws.com/production/gikou?byoyomi=10000&position=sfen lr5nl/2g1kg1s1/p1npppbpp/2ps5/8P/2P3R2/PP1PPPP1N/1SGB1S3/LN1KG3L w 2Pp 1')
# print(r)
# print(r.text)
data = r.json()
print(data['bestmove'])
