from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
   
    return "index\n work in progress\n" 

@app.route('/msg', methods=['GET', 'POST'])
def msg():
    msg = request.args.get('msg', default = 'NULL', type = str)
    uname = request.args.get('uname', default = 'Anon', type = str)
    channel = request.args.get('channel', default = '', type = str)

    if channel == '':
        return "mention the channel please!\n"
    else:
        filename = "data/" + "db-" + channel + ".txt"  
        db = open(filename, "a")
        string = uname + ": "+ msg + "\n"
        db.write(string)
        db.close
        return "message sent!\n"

@app.route('/channel/<name>', methods=['GET', 'POST'])
def chan(name):
    filename = "data/db-" + name + ".txt"
    db = open(filename, "r")
    return db.read()

app.run()
