from flask import Flask, app, render_template, request
from flask_sqlalchemy import SQLAlchemy

from db_users import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:pass@localhost/users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = 'gntvmrtb9ntrh9nrttj9504jyhgmweogmrh49954y864h94bm'
db = SQLAlchemy(app)
app.app_context().push()


@app.route('/')
def index():
    return render_template("index.html", methods=['POST', 'GET'])


# Страница автоизации/регистрации
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
