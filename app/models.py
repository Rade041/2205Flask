import jwt
from time import time
from app import db, login
from datetime import datetime
from flask import current_app
from flask_login import UserMixin
from flask_login import LoginManager # new code entry
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

# timestamp to be inherited by other class models
class TimestampMixin(object):
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

@login.user_loader  # new code entry
def load_user(id):  # new code entry
    return User.query.get(int(id)) # new code entry --- # slightly modified such that the user is loaded based on the id in the db

# user class
class User(db.Model, TimestampMixin, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password_hash = db.Column(db.String(128))
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)

    # print to console username created
    def __repr__(self):
        return f'<User {self.username}>'
    # generate user password i.e. hashing
    def set_password(self, password): 
        self.password_hash = generate_password_hash(password)
    # check user password is correct
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    # for reseting a user password
    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            current_app.config['SECRET_KEY'],
            algorithm='HS256').decode('utf-8')
    # verify token generated for resetting password
    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, current_app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)


class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author_name = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Article {self.title}>'
    
class Jobs(db.Model):
    id = db.Column (db.Integer, primary_key=True, unique=True)
    job_title = db.Column (db.String(150), index=True)
    salary = db.Column(db.Integer, index=True)
    description = db.Column(db.String(500), index=True)
    location = db.Column(db.String(100))
    industry = db.Column(db.String(100))
    sector = db.Column(db.String(100))

    def __repr__(self):
        return '<Jobs {}>' .format(self.Job_Title)
    
class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    course_title = db.Column(db.String(100))
    course_leader = db.Column(db.String(100))
    start_date = db.Column(db.String(100))
    end_date = db.Column(db.String(100))
    venue_name_address = db.Column(db.String(100))
    contact_phone = db.Column(db.String(100))
    contact_email = db.Column(db.String(100))
    description = db.Column(db.String(100))

    def __repr__(self):
        return '<Courses {}>' .format(self.Course_Title)
