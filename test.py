# https://www.youtube.com/watch?v=Z1RJmh_OqeA

from flask import Flask

app = Flask(__name__)

@ app.route('/')
def index():
    return "Hello World 2019!"

if __name__ == "__main__":
    app.run(debug=True)


