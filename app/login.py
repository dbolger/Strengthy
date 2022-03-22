from app import app
from database import database_get
from flask_login import LoginManager, UserMixin, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email

# https://python.plainenglish.io/implementing-flask-login-with-hash-password-888731c88a99

# Forms classes for flask_wtf
class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    remember_me = BooleanField()

class RegisterForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    name = StringField("name")
    email = StringField("email", validators=[DataRequired(), Email()])

# User class for flask_login
class User(UserMixin):
    def __init__(self, id, email, password_hash):
        self.id = unicode(id)
        self.email = email
        self.password_hash = password_hash
        self.authenticated = False

    def is_authenticated(self):
        return self.authenticated

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(uid):
    conn = database_get()
    curs = conn.cursor()
    curs.execute("SELECT * FROM users WHERE id = (?)", [uid])
    row = curs.fetchone()

    if row is None:
        return None
    else:
        return User(int(row[0]), row[1], row[2])
