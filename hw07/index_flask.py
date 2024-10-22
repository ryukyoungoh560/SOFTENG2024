from flask import Flask, render_template

from datetime import datetime


app = Flask(__name__)

posts = [
    {
        "author": {"username": ""},
        "title": "hw07",
        "content": "7번째 과제입니다",
        "date_posted": datetime.strptime("2024-10-03", "%Y-%m-%d"),
    },
]


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/blog")
def blog():
    return render_template("blog.html", title="Blog")


app.run(debug=True)

# if __name__ == '__main__':
# app.run(host="0.0.0.0", debug=True)
