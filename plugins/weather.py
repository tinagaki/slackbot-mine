from slackbot.bot import respond_to
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ
#import slackbot_settings
import urllib
import json
import requests
import datetime
# 天気関連
def requestWeather():
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city='
    # '130010'とすると東京の情報を取得してくれる
    # ここを変えれば任意の地域の天気情報を取得できる
    city_id = '130010'
    html = urllib.request.urlopen(url + city_id)
    jsonfile = json.loads(html.read().decode('utf-8'))
    return jsonfile

def makeWeatherIcon(telop):
    if telop.find('雪') > -1:
        telop_icon = ':showman:'
    elif telop.find('雷') > -1:
        telop_icon = ':thinder_cloud_and_rain:'
    elif telop.find('晴') > -1:
        if telop.find('曇') > -1:
            telop_icon = ':partly_sunny:'
        elif telop.find('雨') > -1:
            telop_icon = ':partly_sunny_rain:'
        else:
            telop_icon = ':sunny:'
    elif telop.find('雨') > -1:
        telop_icon = ':umbrella:'
    elif telop.find('曇') > -1:
        telop_icon = ':cloud:'
    else:
        telop_icon = ':fire:'
    return telop_icon

@respond_to(r'^今日の天気[は|？]?')
@respond_to('今日の天気は？')
def weatherToday(message):
    jsonfile = requestWeather()
    title = jsonfile['title']
    print(jsonfile['forecasts'])
    telop = jsonfile['forecasts'][0]['telop']
    date = jsonfile['forecasts'][0]['date']
    #telopが晴れだったら晴れのスラックのアイコンとか場合分け
    telop_icon = ''
    telop_icon = makeWeatherIcon(telop)
    text = title + '\n' + '今日の天気('+ date +')　' + telop + telop_icon
    message.send(text)

@respond_to(r'^明日の天気[は|？]?')
@respond_to('明日の天気は？')
def weatherToday(message):
    jsonfile = requestWeather()
    title = jsonfile['title']
    print(jsonfile['forecasts'])
    telop = jsonfile['forecasts'][1]['telop']
    date = jsonfile['forecasts'][1]['date']
    #telopが晴れだったら晴れのスラックのアイコンとか場合分け
    telop_icon = ''
    telop_icon = makeWeatherIcon(telop)
    text = title + '\n' + '明日の天気('+ date +')　' + telop + telop_icon
    message.send(text)
# !天気関連
