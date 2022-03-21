from app import app
from database import database_get
from flask_login import LoginManager, UserMixin, current_user

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
