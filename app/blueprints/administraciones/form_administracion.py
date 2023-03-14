from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AdministracionForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    contacto = StringField('Contacto')
    codigoSelae = StringField('Codigo Selae', validators=[DataRequired()])
    submit = SubmitField('Submit')