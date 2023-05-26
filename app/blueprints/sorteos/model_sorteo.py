#!/usr/bin/python
from app import db
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.exc import IntegrityError
from datetime import datetime


class Sorteo(db.Model):
    __tablename__ = 'sorteos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    fecha_sorteo = db.Column(db.String(20))
    dia_semana = db.Column(db.String(10))
    tipo_sorteo = db.Column(db.String(20))
    id_sorteo = db.Column(db.Integer, unique=True)
    game_id = db.Column(db.String(5))
    anyo = db.Column(db.Integer)
    numero_sorteo = db.Column(db.Integer)
    lugar =  db.Column(db.String(100))
    premio_bote = db.Column(db.Integer)
    cdc = db.Column(db.Integer)
    apuestas = db.Column(db.Integer)
    recaudacion = db.Column(db.Integer)
    combinacion_json = db.Column(JSON)
    premios = db.Column(db.Integer)
    fondo_bote = db.Column(db.Integer)
    escrutinio = db.Column(JSON)
    
        
    def __repr__(self):
        return f'<Sorteo {self.nombre}>'

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
        return Sorteo.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Sorteo.query.get(id)

    @staticmethod
    def get_tipo_sorteo(tipo_sorteo):
        return Sorteo.query.filter(Sorteo.game_id==tipo_sorteo).all()
    
    @staticmethod
    def exists(id_sorteo):
        result = Sorteo.query.filter(Sorteo.id_sorteo == id_sorteo)
        if result:
            for sorteo in result:
                return sorteo.id
        else: return False
    
    @staticmethod
    def get_by_id_sorteo(id_sorteo):
        return Sorteo.query.get(id_sorteo)
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    @staticmethod
    def all_paginated(page=1, per_page=20):
        return Sorteo.query.order_by(Sorteo.fecha_sorteo.desc()).\
            paginate(page=page, per_page=per_page, error_out=False)

class LoteriaNacionalCombinacion(db.Model):
    #__tablename__ = 'loteria_nacional_combinacion'
    id = db.Column(db.Integer, primary_key=True)
    sorteo_id = db.Column(db.Integer, db.ForeignKey('sorteos.id'),nullable=False, unique=True)
    primer_premio = db.Column(db.Integer)
    segundo_premio = db.Column(db.Integer)
    tercer_premio = db.Column(db.Integer)
    cuarto_premio = db.Column(db.Integer)
    quinto_premio = db.Column(db.Integer)
    fraccion = db.Column(db.Integer)
    serie = db.Column(db.Integer)

class BonolotoCombinacion(db.Model):
    #__tablename__ = 'consginaciones'
    id = db.Column(db.Integer, primary_key=True)
    sorteo_id = db.Column(db.Integer, db.ForeignKey('sorteos.id'),nullable=False)
    bola_1 = db.Column(db.Integer)
    bola_2 = db.Column(db.Integer)
    bola_3 = db.Column(db.Integer)
    bola_4 = db.Column(db.Integer)
    bola_5 = db.Column(db.Integer)
    bola_6 = db.Column(db.Integer)
    reintegro = db.Column(db.Integer)
    complementario = db.Column(db.Integer)

class PrimitivaCombinacion(db.Model):
    #__tablename__ = 'consginaciones'
    id = db.Column(db.Integer, primary_key=True)
    sorteo_id = db.Column(db.Integer, db.ForeignKey('sorteos.id'),nullable=False)
    bola_1 = db.Column(db.Integer)
    bola_2 = db.Column(db.Integer)
    bola_3 = db.Column(db.Integer)
    bola_4 = db.Column(db.Integer)
    bola_5 = db.Column(db.Integer)
    bola_6 = db.Column(db.Integer)
    reintegro = db.Column(db.Integer)
    complementario = db.Column(db.Integer)

class EuromillonesCombinacion(db.Model):
    #__tablename__ = 'consginaciones'
    id = db.Column(db.Integer, primary_key=True)
    sorteo_id = db.Column(db.Integer, db.ForeignKey('sorteos.id'),nullable=False)
    bola_1 = db.Column(db.Integer)
    bola_2 = db.Column(db.Integer)
    bola_3 = db.Column(db.Integer)
    bola_4 = db.Column(db.Integer)
    bola_5 = db.Column(db.Integer)
    estrella_1 = db.Column(db.Integer)
    estrella_2 = db.Column(db.Integer)

class GordoPrimitivaCombinacion(db.Model):
    #__tablename__ = 'consginaciones'
    id = db.Column(db.Integer, primary_key=True)
    sorteo_id = db.Column(db.Integer, db.ForeignKey('sorteos.id'),nullable=False)
    bola_1 = db.Column(db.Integer)
    bola_2 = db.Column(db.Integer)
    bola_3 = db.Column(db.Integer)
    bola_4 = db.Column(db.Integer)
    bola_5 = db.Column(db.Integer)
    clave = db.Column(db.Integer)

class QuinielaPartidos(db.Model):
    #__tablename__ = 'consginaciones'
    id = db.Column(db.Integer, primary_key=True)
    sorteo_id = db.Column(db.Integer, db.ForeignKey('sorteos.id'),nullable=False)
    local = db.Column(db.String(60))
    visitante = db.Column(db.String(60))
    signo = db.Column(db.String(8))
    local = db.Column(db.String(8))

class QuinigolPartidos(db.Model):
    #__tablename__ = 'consginaciones'
    id = db.Column(db.Integer, primary_key=True)
    sorteo_id = db.Column(db.Integer, db.ForeignKey('sorteos.id'),nullable=False)
    local = db.Column(db.String(60))
    visitante = db.Column(db.String(60))
    signo = db.Column(db.String(8))
    local = db.Column(db.String(8))

class LototurfCombinacion(db.Model):
    #__tablename__ = 'consginaciones'
    id = db.Column(db.Integer, primary_key=True)
    sorteo_id = db.Column(db.Integer, db.ForeignKey('sorteos.id'),nullable=False)
    bola_1 = db.Column(db.Integer)
    bola_2 = db.Column(db.Integer)
    bola_3 = db.Column(db.Integer)
    bola_4 = db.Column(db.Integer)
    bola_5 = db.Column(db.Integer)
    bola_6 = db.Column(db.Integer)
    caballo = db.Column(db.Integer)
    reintegro = db.Column(db.Integer)
    
class QuintupleplusCombinacion(db.Model):
    #__tablename__ = 'consginaciones'
    id = db.Column(db.Integer, primary_key=True)
    sorteo_id = db.Column(db.Integer, db.ForeignKey('sorteos.id'),nullable=False)
    bola_1 = db.Column(db.Integer)
    bola_2 = db.Column(db.Integer)
    bola_3 = db.Column(db.Integer)
    bola_4 = db.Column(db.Integer)
    bola_5 = db.Column(db.Integer)
    bola_6 = db.Column(db.Integer)