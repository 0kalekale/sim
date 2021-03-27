from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    return "werks"

app.run()
