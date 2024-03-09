# Import
from flask import Flask, render_template,request, redirect
from datetime import *
import datetime, tkinter
from tkinter import *
import tkinter as tk

app = Flask(__name__)

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    su_anki_yil = int(datetime.datetime.year())
    yas = su_anki_yil - 2012
    return render_template('main_index.html', yasim=yas)


# Dinamik beceriler
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    return render_template('index.html', button_python=button_python)


if __name__ == "__main__":
    app.run(debug=True)
