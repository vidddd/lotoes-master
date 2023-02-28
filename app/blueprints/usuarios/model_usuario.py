#from flask_login import UserMixin
#from flask_login import login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))
    email = db.Column(db.String(100))
    is_admin = db.Column(db.Boolean)
    created = db.Column(db.DateTime)
    updated = db.Column(db.DateTime)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    
    def __repr__(self):
        return '<User %r>' % self.username
    
    def __init__(self, id, nombre, password, email, is_admin=False):
        self.id = id
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
        self.is_admin = is_admin
        created = datetime.now()
        updated = datetime.now()
        
    def save(self):
        if not self.id:
            db.session.add(self)
        saved = False
        count = 0
        while not saved:
            try:
                db.session.commit()
                saved = True
            except IntegrityError:
                print(IntegrityError)
                count += 1

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return Usuario.query.get(id)

    @staticmethod
    def get_by_email(email):
        return Usuario.query.filter_by(email=email).first()

    @staticmethod
    def get_all():
        return Usuario.query.all()


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('Usuario', backref='role')
    
    def __repr__(self):
        return '<Role %r>' % self.name

#@login_manager.user_loader
#def load_user(user_id):
#    return Usuario.query.get(int(user_id))