from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length
from config.lotoes_config import tipos_sorteo

class ImporterForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=100)])
    nombre_sistema = StringField('Nombre Sistema', validators=[Length(max=100)])
    tipo_sorteo = SelectField('Tipo Sorteo', choices=tipos_sorteo, validators=[DataRequired()])
    url = StringField('Url', validators=[DataRequired(), Length(max=200)])
    actualizar_existentes= BooleanField('Actualizar Existentes?')
    parametro_fecha= BooleanField('Parámetro Fecha')
    dias = IntegerField('Dias', default=0)
    activo= BooleanField('Activo')
    submit = SubmitField('Submit')

class ImporterSearchForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=100)])
    tipo_sorteo = SelectField('Tipo Sortero:', choices=tipos_sorteo)
    activo= BooleanField('Activo')
    search = StringField('')