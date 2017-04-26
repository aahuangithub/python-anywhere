
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config["DEBUG"] = True

#used to init database
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://aahuang:pythonanywhere@aahuang.mysql.pythonanywhere-services.com/aahuang$default".format(
    username="aahuang",
    password="pythonanywhere",
    hostname="aahuang.mysql.pythonanywhere-services.com",
    databasename="aahuang$default",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
db = SQLAlchemy(app)

#https://imgur.com/gallery/FJGiw
#https://blog.pythonanywhere.com/121/
class Event(db.Model):
    __tablename__="events"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(2048))
    date = db.Column(db.String(64))
    content = db.Column(db.Text())
    links = db.Column(db.Text())
    def __init__(self, t, c, l, d=None):
        self.title=t
        self.content=c
        self.links=l
        if d is None:
            self.d='hello'
    def __str__(self):
        return self.t
events=[]

@app.route('/')
def index():
    return render_template('/index.html') # ... uses jinja2 templates

@app.route('/layout')
def layout():
    return render_template('/layout.html')

@app.route('/hello-world')
def hello_world():
    return 'Hello flask!'

@app.route('/editor', methods={'GET', 'POST'})
def editor():
    return render_template('/editor.html')

@app.route('/num/<int:num>') #type your parameters!!!
def show_num(num):
    return 'Your number is %i.' %num

if __name__ == "__main__":
    app.run()


