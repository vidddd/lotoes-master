from sqlalchemy.exc import IntegrityError
from app import db
from datetime import datetime

class Administracion(db.Model):
    __tablename__ = 'administraciones'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(256), nullable=False)
    contacto = db.Column(db.String(256))
    codigoSelae = db.Column(db.Integer, nullable=False)
    telefono = db.Column(db.String(15))
    movil = db.Column(db.String(15))
    email = db.Column(db.String(100))
    web = db.Column(db.String(150))
    direccion = db.Column(db.String(256))
    municipio = db.Column(db.String(256))
    cp = db.Column(db.Integer, nullable=False)
    notas = db.Column(db.Text)
    provincia_id = db.Column(db.SmallInteger, db.ForeignKey('provincias.id', ondelete='CASCADE'))
    provincia = db.relationship('Provincia',backref=db.backref('provincias', lazy=True))
    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime)

    def __repr__(self):
        return f'<Administracion {self.nombre}>'

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
                count += 1
                
    @staticmethod
    def get_all():
        return Administracion.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Administracion.query.get(id)

    @staticmethod
    def all_paginated(page=1, per_page=20):
        return Administracion.query.order_by(Administracion.id.desc()).\
            paginate(page=page, per_page=per_page, error_out=False)