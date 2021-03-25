import flask
from flask import request
posts = []

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/feed', methods=["GET"])
def feed():
    post = '<br>'.join(posts)
    return post

@app.route('/add_post', methods=["GET"])
def add():
    print(request.query_string)
    post = str(request.query_string)[2:-1]
    posts.append(post)
    return post

app.run(
    host='127.0.0.1'
)
