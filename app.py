from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
   
    return '''
<center>
=========================<br>
SIM<br>
=========================<br>
<br>
Simple Internet messenger<br>
<br>
A simple IM, based on HTTP/S protocol. implemented in Python3/Flask<br>
<center>
<br>
<a href='client'>example SIM client ($ curl http://url.com/client > client.py)</a>
''' 

@app.route('/msg', methods=['GET', 'POST'])
def msg():
    msg = request.args.get('msg', default = 'NULL', type = str)
    uname = request.args.get('uname', default = 'Anon', type = str)
    channel = request.args.get('channel', default = '', type = str)
    
    if channel == '':
        return "mention the channel please!\n"
    else:
        if msg == 'NULL':
            return 'include a message!\n'
        else:
            filename = "data/" + "db-" + channel + ".txt"  
            db = open(filename, "a")
            string = uname + ": "+ msg + "\n"
            db.write(string)
            db.close
            return "200"
    

@app.route('/channel/<name>', methods=['GET', 'POST'])
def chan(name):
    filename = "data/db-" + name + ".txt"
    db = open(filename, "r")
    return db.read()

@app.route('/client')
def cli():
    return open('client.py', 'r').read()
@app.errorhandler(404)
def page_not_found(e):
    return 'e404', 404
@app.errorhandler(500)
def server_error(e):
    return 'e500', 500
app.run()
