from flask import render_template
from app import flask_app

@flask_app.route("/")
@flask_app.route("/index")
def index():
    user = {"username": "Jonathan"}
    posts = [
        {
            "author": {"username": "Catherine"},
            "content": "The AI boom is real"
        }, 
        {
            "author": {"username": "Melinda"},
            "content": "Weather is gloomy all day"
        },
    ]
    return render_template("index.html", user=user, posts=posts)
