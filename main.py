from flask import Flask
from flask import render_template, url_for
from forms import FindStatusForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '1234'

notifications = [ (i,'Finance Notification '+ str(i)) for i in range(1,16)]

@app.route("/")
def home():
    return render_template('home.html',pagetitle="Home Page")

@app.route("/details/<type>")
def details(type):
    return render_template('details.html',pagetitle="Detail Page",notifications=notifications,type=type)

@app.route("/findstatus")
def findstatus():
    form = FindStatusForm()
    return render_template('findstatus.html',pagetitle="Find Status",form=form)

app.run(debug=True)    