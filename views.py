from main import app
from flask import render_template

# rotas 

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cadastro.html")
def cadastro():
    return render_template("cadastro.html")

@app.route("/login.html")
def login():
    return render_template("login.html")

@app.route("/reserva.html")
def reserva():
    return render_template("reserva.html")