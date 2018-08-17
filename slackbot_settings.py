# coding: UTF-8
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Slack API
API_TOKEN =  os.environ.get("API_TOKEN")

# Docomo対話API
DOCOMO_API_KEY = os.environ.get("DOCOMO_API_KEY")
DOCOMO_APP_ID = os.environ.get("DOCOMO_APP_ID")



# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "理解が難しい文章です。"

PLUGINS = [
    'plugins',
]
