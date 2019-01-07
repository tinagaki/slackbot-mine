
import urllib
import json
import requests
import datetime
#https://api.apigw.smt.docomo.ne.jp/naturalChatting/v1/registration


#エンドポイントの設定
url = 'https://api.apigw.smt.docomo.ne.jp/naturalChatting/v1/registration?APIKEY=XXXXXX'

payload = {'language':'ja-JP', 'botId':'Chatting','appKind':"appid"} #変更
headers = {'Content-type': 'application/json'}
#print(json.dumps(payload))
#送信
r = requests.post(url, data=json.dumps(payload), headers=headers)
data = r.json()

print(data)
