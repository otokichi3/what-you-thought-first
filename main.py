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
　・Hard Working

■プライベート
　・Hard houseworking
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
