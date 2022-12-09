from flask import Flask, render_template 
from flask import redirect
app = Flask(__name__)
@app.route("/")
def greeting():
    return "Hello World!"

@app.route("/flask2")
def fla():
    return "Nice to meet you!"

@app.route("/firstpage")
def firstPage():
    name = "Darvn"
    return render_template("index.html", index_variable=name)

app.run(debug=True)
