from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello():
    html_str = """ 
<!DOCTYPE html>
 <html lang="kr">
 <head>
 <meta charset="UTF-8">
 <script 
src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></scr
 ipt>
 </head>
 <body>
 <form id="form_id" action="javascript:post_query()">
 <input type="text" name="dan" value="7">
 <button type="submit">Go</button>
 </form>
 <div id="results"></div>
 <script>
 function post_query() {
 $.ajax({
 type: "GET",
 url: "http://localhost:5000/gugudan",
 data: $("#form_id").serialize(),
 success: update_result,
 dataType: "html"
 });
 }
 function update_result(data) {
 $("#results").html(data);
 }
 </script>
 </body>
 </html>
"""
    return html_str
#아직 미완성, 페이지를 넘겨서 실행되도록 하는 거

@app.route("/hello/<name>")
def say_hello(name):
    return f"안녕하세요. {escape(name)}님"

@app.route("/dan/<dan>")
def gugudan_html(dan):
    html_str = ""
    for i in range(1,10):
        html_str += f"{dan} X {i} = {int(dan)*i}<br>"
    return html_str

@app.route("/gugudan/")
def gugudan_arg_html():
    dan = request.args.get("dan", "2")
    html_str = ""
    for i in range(1,10):
        html_str += f"{dan} X {i} = {int(dan)*i}<br>"
    return html_str

app.run(debug=True)