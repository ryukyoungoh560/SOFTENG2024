from flask import Flask, render_template

from datetime import datetime

 
app = Flask(__name__)
 
posts = [
    {
        'author': {
            'username': 'test-user'
        },
        'title': '첫 번째 포스트',
        'content': '첫 번째 포스트 내용입니다.',
        'date_posted': datetime.strptime('2024-10-03', '%Y-%m-%d')
    },
    {
        'author': {
            'username': 'test-user'
        },
        'title': '두 번째 포스트',
        'content': '두 번째 포스트 내용입니다.',
        'date_posted': datetime.strptime('2024-10-03', '%Y-%m-%d')
    },
]

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about_me')
def about_me():
    return render_template('about_me.html', title = 'About')

@app.route('/blog_list')
def blog_list():
    return render_template('blog_list.html')

app.run(debug=True)