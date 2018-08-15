'''
    Multiple controllers:
        https://stackoverflow.com/questions/15231359/split-python-flask-app-into-multiple-files
'''

from flask import Flask
from AccountAPI import account_api

app = Flask(__name__)

app.register_blueprint(account_api)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()