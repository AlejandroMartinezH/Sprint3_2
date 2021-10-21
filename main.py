from flask import Flask, render_template, request, flash

app = Flask(__name__)

@app.route('/')
def pruebas():
    return render_template("usuario_final.html")
