import os
from app import app

# Create admin user by defing fab options
cmd = 'flask fab create-admin --username admin --firstname admin --lastname user --email admin@3dapp.org --password admin'
os.system(cmd)

app.run(host="0.0.0.0", port=5000, debug=True)