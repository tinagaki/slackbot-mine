from slackbot.bot import respond_to
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ
#import slackbot_settings
import urllib
import json
import requests
import datetime
import slackbot_settings




@respond_to('こんにちは')
@respond_to('今日は')
def hello(message):
    message.reply('こんにちは!')

@default_reply()
def docomo_talk_default(message):
    """
    Docomo自然対話APIから返答する
    """


    #エンドポイントの設定
    endpoint = 'https://api.apigw.smt.docomo.ne.jp/naturalChatting/v1/dialogue?APIKEY=REGISTER_KEY'
    appid = slackbot_settings.DOCOMO_APP_ID
    docomo_api_key = slackbot_settings.DOCOMO_API_KEY
    url = endpoint.replace('REGISTER_KEY', docomo_api_key)

    now = datetime.datetime.today()
    text = message.body['text']
    payload = {'language':'ja-JP', 'botId':'Chatting','appId':appid,'voiceText':text} #変更
    headers = {'Content-type': 'application/json'}
    #print(json.dumps(payload))
    #送信
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    data = r.json()

    print(data)
    #jsonの解析
    response = data['systemText']['utterance'] #変更

    #表示
    message.reply('%s' % response)


def recruit_talk_default(message):
    none

