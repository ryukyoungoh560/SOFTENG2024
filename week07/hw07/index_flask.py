from flask import Flask, render_template

from datetime import datetime

import pandas as pd 


app = Flask(__name__)
 
posts = [
    {
        'author': {
            'username': '오류경'
        },
        'title': 'first',
        'content': '7번째 과제입니다',
        'date_posted': datetime.strptime('2024-10-17', '%Y-%m-%d')
    },
    {
        'author': {
            'username': ''
        },
        'title': 'second',
        'content': '7week',
        'date_posted': datetime.strptime('2024-10-17', '%Y-%m-%d')
    },
]
# df = pd.read_csv("data.csv")  csv파일 읽어서 자동완성(?)
# post_list = df.to_dict(orient='records')

for i,row in df.iterrows():
    post.append({
        "title": row['title'],
        "content": row['content'] 
    })

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title = 'Post', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

@app.route('/blog')
def blog():
    return render_template('blog.html', title = 'Blog')

app.run(debug=True)

#if __name__ == '__main__':
    #app.run(host="0.0.0.0", debug=True)