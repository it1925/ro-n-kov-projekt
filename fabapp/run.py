import os
from app import app

cmd = 'flask fab create-admin --username admin --firstname admin --lastname user --email admin@3dapp.org --password admin'
os.system(cmd)

app.run(host="0.0.0.0", port=8080, debug=True)