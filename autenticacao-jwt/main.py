from datetime import datetime, timedelta, timezone
from flask import Flask, jsonify
import jwt
import os
from dotenv import load_dotenv

os.system('clear')
os.system('pip list')
print('')
load_dotenv()

app = Flask(__name__)

@app.route('/secret', methods=['POST'])
def secret():
    return jsonify({'secret': 'small dick!'}), 200

@app.route('/', methods=['POST'])
def login():
    token = jwt.encode({'user': 'admin', 'exp': datetime.now(timezone.utc) + timedelta(minutes=1)}, 'secret', algorithm='HS256')

    return jsonify({'token': token}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)