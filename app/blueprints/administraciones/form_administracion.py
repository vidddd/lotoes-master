from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AdministracionForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    contacto = StringField('Contacto')
    codigoSelae = StringField('Codigo Selae', validators=[DataRequired()])
    telefono = StringField('Telefono')
    movil = StringField('Movil')
    email = StringField('Email')
    web = StringField('Web')
    direccion = StringField('Direccion')
    municipio = StringField('Municipio')
    cp = StringField('Cp')
    submit = SubmitField('Submit')