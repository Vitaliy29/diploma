import os
from flask import *
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import *
from datetime import datetime
import yaml

# Конфигурация
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:pass@localhost/users'
# app.config['SECRET_KEY'] = 'gntvmrtb9ntrh9n87"№"%rttj9504jyhgmweogmrh49954y864h94bm'
db = yaml.safe_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html', methods=['POST', 'GET'])


@app.route('/webapp', methods=['POST', 'GET'])
def webapp():
    return render_template('webapp.html', methods=['POST', 'GET'], title="Приложение")


# СТРАНИЦА РЕГИСТРАЦИИ
@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['psw']
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO users(name, email, psw) VALUES (%s, %s, %s)",
            (name, email, password))
        mysql.connection.commit()
        cur.close()
        return "SUCCESS"
        # item = Item(name=name, email=email, password=password)

    return render_template('signup.html', methods=['POST', 'GET'])


# СТРАНИЦА ВХОДА
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['psw']
    if 'userLogged' in session:
        return redirect(url_for('webapp', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == "vit1000" and request.form['psw'] == "123123":
        session['userLogged'] = request.form['username']
        return redirect(url_for('webapp', username=session['userLogged']))
    return render_template('login.html', methods=['POST', 'GET'], title="Приложение")


if __name__ == '__main__':
    app.run(debug=True)
