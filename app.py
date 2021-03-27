from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    db = open("data/db.txt", "rb").read()
    return db

@app.route('/msg', methods=['GET', 'POST'])
def msg():
    msg = request.args.get('msg', default = '', type = str)
    uname = request.args.get('uname', default = '', type = str)
    db = open("data/db.txt", "a")
    string = uname + ": "+ msg + "\n"
    db.write(string)
    db.close
    return "message sent!\n"
app.run()
