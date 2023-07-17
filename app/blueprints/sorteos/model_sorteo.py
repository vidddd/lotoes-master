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
        return f'<Sorteo {self.id_sorteo}>'

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
    def get_tipo_sorteo(tipo_sorteo, page=1, per_page=20):
        return Sorteo.query.filter(Sorteo.game_id==tipo_sorteo).order_by(Sorteo.fecha_sorteo.desc()).\
            paginate(page=page, per_page=per_page, error_out=False)
    
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
    sorteo = db.relationship(Sorteo, backref="loteria_nacional_combinacion")
    primer_premio = db.Column(db.Integer)
    segundo_premio = db.Column(db.Integer)
    tercer_premio = db.Column(db.Integer)
    cuarto_premio = db.Column(db.Integer)
    quinto_premio = db.Column(db.Integer)
    fraccion = db.Column(db.Integer)
    serie = db.Column(db.Integer)

    def __repr__(self):
        return f'<LoteriaNacionalCombinacion {self.id}>'

    @staticmethod
    def exists_by_sorteo_id(sorteo_id):
        result = LoteriaNacionalCombinacion.query.filter(LoteriaNacionalCombinacion.sorteo_id == sorteo_id)
        if result:
            for sorteo in result:
                return sorteo.id
        else: return False

class BonolotoCombinacion(db.Model):
    #__tablename__ = 'bonoloto_combinacion'
    id = db.Column(db.Integer, primary_key=True)
    sorteo_id = db.Column(db.Integer, db.ForeignKey('sorteos.id'),nullable=False)
    sorteo = db.relationship(Sorteo, backref="bonoloto_combinacion", uselist=False)
    bola_1 = db.Column(db.Integer)
    bola_2 = db.Column(db.Integer)
    bola_3 = db.Column(db.Integer)
    bola_4 = db.Column(db.Integer)
    bola_5 = db.Column(db.Integer)
    bola_6 = db.Column(db.Integer)
    reintegro = db.Column(db.Integer)
    complementario = db.Column(db.Integer)

    def __repr__(self):
        return f'<BonolotoCombinacion {self.id}>'

    @staticmethod
    def exists_by_sorteo_id(sorteo_id):
        result = BonolotoCombinacion.query.filter(BonolotoCombinacion.sorteo_id == sorteo_id)
        if result:
            for sorteo in result:
                return sorteo.id
        else: return False

class PrimitivaCombinacion(db.Model):
    #__tablename__ = 'primitiva_combinacion'
    id = db.Column(db.Integer, primary_key=True)
    sorteo_id = db.Column(db.Integer, db.ForeignKey('sorteos.id'),nullable=False)
    sorteo = db.relationship(Sorteo, backref="primitiva_combinacion")
    bola_1 = db.Column(db.Integer)
    bola_2 = db.Column(db.Integer)
    bola_3 = db.Column(db.Integer)
    bola_4 = db.Column(db.Integer)
    bola_5 = db.Column(db.Integer)
    bola_6 = db.Column(db.Integer)
    reintegro = db.Column(db.Integer)
    complementario = db.Column(db.Integer)

    def __repr__(self):
        return f'<PrimitivaCombinacion {self.id}>'

    @staticmethod
    def exists_by_sorteo_id(sorteo_id):
        result = PrimitivaCombinacion.query.filter(PrimitivaCombinacion.sorteo_id == sorteo_id)
        if result:
            for sorteo in result:
                return sorteo.id
        else: return False

class EuromillonesCombinacion(db.Model):
    #__tablename__ = 'euromillones_combinacion'
    id = db.Column(db.Integer, primary_key=True)
    sorteo_id = db.Column(db.Integer, db.ForeignKey('sorteos.id'),nullable=False)
    sorteo = db.relationship(Sorteo, backref="euromillones_combinacion")
    bola_1 = db.Column(db.Integer)
    bola_2 = db.Column(db.Integer)
    bola_3 = db.Column(db.Integer)
    bola_4 = db.Column(db.Integer)
    bola_5 = db.Column(db.Integer)
    estrella_1 = db.Column(db.Integer)
    estrella_2 = db.Column(db.Integer)

    def __repr__(self):
        return f'<EuromillonesCombinacion {self.id}>'

    @staticmethod
    def exists_by_sorteo_id(sorteo_id):
        result = EuromillonesCombinacion.query.filter(EuromillonesCombinacion.sorteo_id == sorteo_id)
        if result:
            for sorteo in result:
                return sorteo.id
        else: return False

class GordoPrimitivaCombinacion(db.Model):
    #__tablename__ = 'gordo_primitiva_combinacion'
    id = db.Column(db.Integer, primary_key=True)
    sorteo_id = db.Column(db.Integer, db.ForeignKey('sorteos.id'),nullable=False)
    sorteo = db.relationship(Sorteo, backref="gordo_primitiva_combinacion")
    bola_1 = db.Column(db.Integer)
    bola_2 = db.Column(db.Integer)
    bola_3 = db.Column(db.Integer)
    bola_4 = db.Column(db.Integer)
    bola_5 = db.Column(db.Integer)
    clave = db.Column(db.Integer)

    def __repr__(self):
        return f'<GordoPrimitivaCombinacion {self.id}>'

    @staticmethod
    def exists_by_sorteo_id(sorteo_id):
        result = GordoPrimitivaCombinacion.query.filter(GordoPrimitivaCombinacion.sorteo_id == sorteo_id)
        if result:
            for sorteo in result:
                return sorteo.id
        else: return False

class QuinielaPartidos(db.Model):
    #__tablename__ = 'quiniela_partidos'
    id = db.Column(db.Integer, primary_key=True)
    sorteo_id = db.Column(db.Integer, db.ForeignKey('sorteos.id'),nullable=False)
    sorteo = db.relationship(Sorteo, backref="quiniela_partidos")
    local = db.Column(db.String(60))
    visitante = db.Column(db.String(60))
    signo = db.Column(db.String(8))
    marcador = db.Column(db.String(8))
    fecha = db.Column(db.String(100))

    def __repr__(self):
        return f'<QuinielaPartidos {self.id}>'

    @staticmethod
    def exists_by_sorteo_id(sorteo_id):
        result = QuinielaPartidos.query.filter(QuinielaPartidos.sorteo_id == sorteo_id)
        if result:
            for sorteo in result:
                return sorteo.id
        else: return False

class QuinigolPartidos(db.Model):
    #__tablename__ = 'quinigol_partidos'
    id = db.Column(db.Integer, primary_key=True)
    sorteo_id = db.Column(db.Integer, db.ForeignKey('sorteos.id'),nullable=False)
    sorteo = db.relationship(Sorteo, backref="quinigol_partidos")
    local = db.Column(db.String(60))
    visitante = db.Column(db.String(60))
    signo = db.Column(db.String(8))
    marcador = db.Column(db.String(8))
    fecha = db.Column(db.String(100))

    def __repr__(self):
        return f'<QuinigolPartidos {self.id}>'

    @staticmethod
    def exists_by_sorteo_id(sorteo_id):
        result = QuinigolPartidos.query.filter(QuinigolPartidos.sorteo_id == sorteo_id)
        if result:
            for sorteo in result:
                return sorteo.id
        else: return False

class LototurfCombinacion(db.Model):
    #__tablename__ = 'lototurf_combinacion'
    id = db.Column(db.Integer, primary_key=True)
    sorteo_id = db.Column(db.Integer, db.ForeignKey('sorteos.id'),nullable=False)
    sorteo = db.relationship(Sorteo, backref="lototurf_combinacion")
    bola_1 = db.Column(db.Integer)
    bola_2 = db.Column(db.Integer)
    bola_3 = db.Column(db.Integer)
    bola_4 = db.Column(db.Integer)
    bola_5 = db.Column(db.Integer)
    bola_6 = db.Column(db.Integer)
    caballo = db.Column(db.Integer)
    reintegro = db.Column(db.Integer)

    def __repr__(self):
        return f'<LototurfCombinacion {self.id}>'
    
    @staticmethod
    def exists_by_sorteo_id(sorteo_id):
        result = LototurfCombinacion.query.filter(LototurfCombinacion.sorteo_id == sorteo_id)
        if result:
            for sorteo in result:
                return sorteo.id
        else: return False
    
class QuintupleplusCombinacion(db.Model):
    #__tablename__ = 'quintuple_plus_combinacion'
    id = db.Column(db.Integer, primary_key=True)
    sorteo_id = db.Column(db.Integer, db.ForeignKey('sorteos.id'),nullable=False)
    sorteo = db.relationship(Sorteo, backref="quintuple_plus_combinacion")
    bola_1 = db.Column(db.Integer)
    bola_2 = db.Column(db.Integer)
    bola_3 = db.Column(db.Integer)
    bola_4 = db.Column(db.Integer)
    bola_5 = db.Column(db.Integer)
    bola_6 = db.Column(db.Integer)

    def __repr__(self):
        return f'<QuintupleplusCombinacion {self.id}>'
    
    @staticmethod
    def exists_by_sorteo_id(sorteo_id):
        result = QuintupleplusCombinacion.query.filter(QuintupleplusCombinacion.sorteo_id == sorteo_id)
        if result:
            for sorteo in result:
                return sorteo.id
        else: return False