from flask import Flask, render_template, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bp = Blueprint('blog', __name__)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)


def show_user(username):
    user = User.query.filter_by(username=username).first()
    return f'User {user.username}'


@bp.route('/user/')
def user():
    user = show_user('JohnDoe')  # DBにアクセスして、レコードを取得する
    return render_template('user.html', user=user)


@bp.route('/hello/')
def hello():
    message = "hello"
    return render_template('hello.html', message=message)


app.register_blueprint(bp, url_prefix='/blog')

if __name__ == '__main__':
    app.run(debug=True)
