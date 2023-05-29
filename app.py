from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage   # 載入 TextSendMessage 模組
import json

app = Flask(__name__)

@app.route("/", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)
    json_data = json.loads(body)
    print(json_data)
    try:
        line_bot_api = LineBotApi('9Uu7fzrtqXome+fyLufdqkxI/zdU8+lQQsUSF0cMHrNar6+D2Iq+6Fr5A0hJaTIcxQLoU0OXiKnNrcOWeIUOhfDxLYaqZ3AOZ7RM9i9nMvCGXRwPNgorKSteluLUSEGAATdzA81SYyWqGUfIaqI14wdB04t89/1O/w1cDnyilFU=')
        handler = WebhookHandler('22b3dd5edc00635eec518f2efc897e66')
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)
        tk = json_data['events'][0]['replyToken']         # 取得 reply token
        msg = json_data['events'][0]['message']['text']   # 取得使用者發送的訊息
        text_message = TextSendMessage(text=msg)          # 設定回傳同樣的訊息
        line_bot_api.reply_message(tk,text_message)       # 回傳訊息
    except:
        print('error')
    return 'OK'

if __name__ == "__main__":
    app.run()
