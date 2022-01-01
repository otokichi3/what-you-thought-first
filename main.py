import os
import time
from line_notify_bot import LINENotifyBot
from flask import Flask, make_response, request
from flask_cors import CORS

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def send_thought(request=None):
    start_time = time.perf_counter()
    msg = '''
■仕事
　・毎月20h以上残業
　・Google認定トレーナー
　・積ん読本アウトプット
　・G3は目指さん
　・侍は担当を一人に

■プライベート
　・大阪マラソンサブ４
　・バドは試合出場
　・隔月で読書
　・10h/月は勉強
　・子供（女）
　・啓太を育てる
　・変わらず楽しい家庭に
    '''
    line_token = os.environ['LINE_TOKEN']
    bot = LINENotifyBot(access_token=line_token)
    bot.send(message=msg)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    "process time: {0}".format(elapsed_time)

    return make_response(('OK', 200))

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
