from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    html_str = """ 
<!DOCTYPE html>
<html lang="kr">
<head>
<meta charset="UTF-8">
<title>Flask Home Page</title>
<script 
src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
</head>
<body>
<h2>온도전환하기</h2>

<!-- 섭씨에서 화씨로 전환 -->
<form id = "c2f_form" form method="GET" action="javascript:post_c2f()">
<label>섭씨 => 화씨 :
<input type="text" name="temp">
</label>
<button type="submit">전환</button>
</form>

<!-- 화씨에서 섭씨로 전환 -->
<form id = "f2c_form" form method="GET" action="javascript:post_f2c()">
<label>화씨 => 섭씨 :
<input type="text" name="temp">
</label>
<button type="submit">전환</button>
</form>

<div id="results"></div>

<script>
// 섭씨 => 화씨 변환
function post_c2f() {
$.ajax({
type: "GET",
url: "/c2f",
data: $("#c2f_form").serialize(), 
success: update_result,
dataType: "html"
});
}

// 화씨 => 섭씨 변환
function post_f2c() {
$.ajax({
type: "GET",
url: "/f2c",
data: $("#f2c_form").serialize(), 
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


@app.route("/c2f/")
def c2f_html():
     temp = request.args.get("temp", "0")
     try:
         c2f = (int(temp) * 9 / 5) + 32
         return f"{temp}℃ => {c2f:.2f}℉"
     except ValueError:
         return "숫자를 입력하세요"

@app.route("/f2c/")
def f2c_arg_html():
     temp = request.args.get("temp", "0")
     try:
         f2c = (int(temp) - 32) * 5 / 9
         return f"{temp}℉ => {f2c:.2f}℃"
     except ValueError:
         return "숫자를 입력하세요"

    
app.run(debug=True)
