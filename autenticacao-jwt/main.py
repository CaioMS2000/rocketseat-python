import os
from server import app

os.system('clear')
os.system('pip list')
print('')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)