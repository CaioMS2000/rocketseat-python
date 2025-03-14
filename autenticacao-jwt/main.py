import os
from dotenv import load_dotenv
from flask import Flask, jsonify
from src.models.repositories.mysql.user_repository import MySQLUserRepository
from src.models.settings.db_connection import db_connection_handler

os.system('clear')
os.system('pip list')
print('')
load_dotenv()
db_connection_handler.connect()

app = Flask(__name__)

@app.route('/', methods=['POST'])
def function():

    repo = MySQLUserRepository(db_connection_handler.get_connection())
    print("\n\n")
    print(repo.find_by_id(1))
    print("\n")
    print(repo.list_all())
    print("\n\n")

    return jsonify({'informacao': "pênis grande"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)