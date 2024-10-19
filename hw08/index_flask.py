from flask import Flask, render_template

import os

import pandas as pd 


app = Flask(__name__)

csv_path = os.path.join(app.root_path, 'static', 'csv', 'data.csv') 

df = pd.read_csv(csv_path) 
post_list = df.to_dict(orient='records')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title = 'Post', posts=post_list)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

@app.route('/blog')
def blog():
    return render_template('blog.html', title = 'Blog')



if __name__ == '__main__':
    app.run(debug=True)