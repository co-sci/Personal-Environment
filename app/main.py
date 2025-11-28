from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "<p>This is the main page which will eventually be the landing page</p>"

@app.route("/blog")
def blog():
    return "<p>This is the blog page which will eventually be the daily logs page</p>"