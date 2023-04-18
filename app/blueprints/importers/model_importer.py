#!/usr/bin/python
from app import db
from sqlalchemy.exc import IntegrityError

class Importer(db.Model):
    __tablename__ = 'importers'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    nombre_sistema = db.Column(db.String(100), unique=True)
    tipo_sorteo = db.Column(db.String(20))
    url = db.Column(db.String(200))
    actualizar_existentes = db.Column(db.Boolean)
    parametro_fecha = db.Column(db.Boolean)
    activo = db.Column(db.Boolean)    
    dias = db.Column(db.Integer)
        
    def __repr__(self):
        return f'<Importer {self.nombre}>'

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
        return Importer.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Importer.query.get(id)

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    @staticmethod
    def all_paginated(page=1, per_page=20):
        return Importer.query.order_by(Importer.id.desc()).\
            paginate(page=page, per_page=per_page, error_out=False)