from flask import Blueprint, render_template, redirect, request, current_app, url_for, flash
#from flask_login import login_required
from .model_administraciones import Administracion
from .form_administracion import AdministracionForm

BP_NM = 'administraciones'

administraciones = Blueprint(BP_NM, __name__, template_folder='templates')
 
@administraciones.route('/')
#@login_required
def administraciones_index():
    
    page = int(request.args.get('page', 1))
    administraciones = Administracion.all_paginated(page, current_app.config['ITEMS_PER_PAGE'])
    return render_template('administraciones.html', administraciones=administraciones, seccion="administraciones")

@administraciones.route('/new', methods=['GET','POST'])
#@login_required
def administraciones_new():
    form = AdministracionForm()
    if form.validate_on_submit():
        administracion = Administracion()
        form.populate_obj(administracion)
        administracion.save()
        flash('Administracion añadido correctamente!')
        return redirect(url_for('administraciones.administraciones_index'))
    return render_template('administraciones_new.html', form=form, seccion="administraciones")