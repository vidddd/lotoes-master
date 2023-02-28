#!/usr/bin/python
from app import db
from sqlalchemy.dialects.postgresql import JSON

class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
        
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