from flask import Flask, render_template, request, flash

# creates flask class
app = Flask(__name__)
app.secret_key = "manbeerchicken_SUPER777"

@app.route("/hello")
def index():
    flash("what's your name?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    name = request.form['name_input']
    flash("Hi " + str(name) + ", great to see you!")
    return render_template("index.html")