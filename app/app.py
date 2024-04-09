from flask import Flask, app, render_template, request
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:pass@localhost/users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SECRET_KEY'] = 'gntvmrtb9ntrh9nrttj9504jyhgmweogmrh49954y864h94bm'
db = SQLAlchemy(app)
app.app_context().push()


# У одного сотрудника только 1 профиль
# БД сотрудников. Таблица пользователей
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50), nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)  # Дата регистрации


class Profiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50), nullable=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id')) # Внешний ключ


@app.route('/')
def index():
    return render_template('index.html', methods=['POST', 'GET'])

@app.route('/authorization')
def authorization():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        item = Item(name=name, email=email, password=password)
        
        try:
            db.session.add(item)
            db.session.commit()
            return render_template('authorization.html', methods=['POST', 'GET'])
        except:
            return "ОШИБКА"
    
    else:     
        return render_template('authorization.html', methods=['POST', 'GET'])


'''with app.app_context(): 
    db.create_all() '''
    
    
if __name__ == '__main__':
    app.run(debug=True)
