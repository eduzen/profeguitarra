from flask import Flask
from flask import url_for

app = Flask(__name__)

with app.test_request_context():
    print url_for('index')
    print url_for('login')


if __name__ == '__main__':
    app.debug = True
    app.run()
