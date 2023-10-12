from flask import Flask

app = Flask(__name__)

@app.route('/')

def welcome():
    return "Hi a`m volodia "

if __name__ == '__main__':
    app.run()