#!/usr/bin/python
from app import db
from sqlalchemy.dialects.postgresql import JSON
from datetime import datetime

class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    tipo_cliente = db.Column(db.SmallInteger())
    clasificacion_interna = db.Column(db.SmallInteger())
    es_empresa = db.Column(db.Boolean)
    persona_contacto = db.Column(db.String(256))
    tipo_documento = db.Column(db.SmallInteger(), nullable=False)
    documento = db.Column(db.String(25), nullable=False)
    telefono = db.Column(db.String(15))
    movil = db.Column(db.String(15))
    email = db.Column(db.String(100))
    web = db.Column(db.String(150))
    direccion = db.Column(db.String(256))
    municipio = db.Column(db.String(256))
    provincia = db.Column(db.SmallInteger())
    cp = db.Column(db.Integer())
    pais = db.Column(db.String(100))
    tiene_credito = db.Column(db.Boolean)
    credito = db.Column(db.Float)
    visible = db.Column(db.Boolean)
    saldo = db.Column(db.Float)
    deuda = db.Column(db.Float)
    fecha_nacimiento = db.Column(db.DateTime())
    notas = db.Column(db.Text)
    creado = db.Column(db.DateTime(), default=datetime.utcnow)
    actualizado = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)
    provincia_id = db.Column(db.SmallInteger, db.ForeignKey('provincias.id', ondelete='CASCADE'))
        
    def __repr__(self):
        return f'<Cliente {self.nombre}>'

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
        return Cliente.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Cliente.query.get(id)
    
    @staticmethod
    def exists(id_sorteo):
        result = Cliente.query.filter(Cliente.id_cliente == id_cliente)
        if result:
            for cliente in result:
                return cliente.id
        else: return False
    
    @staticmethod
    def get_by_id_cliente(id_cliente):
        return Cliente.query.get(id_cliente)
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    @staticmethod
    def all_paginated(page=1, per_page=20):
        return Cliente.query.order_by(Cliente.id.desc()).\
            paginate(page=page, per_page=per_page, error_out=False)
    
class Provincia(db.Model):
    __tablename__ = 'provincias'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Provincia {self.nombre}>'
    
    @staticmethod
    def get_all():
        return Provincia.query.all()
    
# used for query_factory    
def getProvincia():
    p = Provincia.query
    return p