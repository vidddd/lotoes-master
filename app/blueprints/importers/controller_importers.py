from flask import Blueprint, render_template, redirect, request, current_app, url_for, flash
import click
from .model_importer import Importer
from .form_importers import ImporterForm
from config.lotoes_config import tipos_sorteo
from app.common.importing_sorteos import ImportingSorteos
from flask_login import login_required

BP_NM = 'importers'
importers = Blueprint(BP_NM, __name__, template_folder='templates')
 
@importers.route('/')
@login_required
def importers_index():
    page = int(request.args.get('page', 1))
    importers = Importer.all_paginated(page, current_app.config['ITEMS_PER_PAGE'])
    return render_template('importers.html', seccion="importers", importers=importers, tipos_sorteo=tipos_sorteo)

""" NEW / EDIT """
@importers.route('/form', methods=['GET', 'POST'], defaults={'importer_id': None})
@importers.route('/form/<int:importer_id>', methods=['GET', 'POST'])
@login_required
def importer_form(importer_id=None):
    if importer_id:
        importer = Importer.get_by_id(importer_id)
        if importer is None:
            raise NotFound(importer_id)
        form = ImporterForm(obj=importer)
    else:
        importer = Importer()
        form = ImporterForm()
    if form.validate_on_submit():
        form.populate_obj(importer)
        importer.save()
        flash('Importer creado / actualizado correctamente!')
        return redirect(url_for('importers.importers_index'))
    return render_template('form_importers.html', form=form, seccion='importers')


""" ACTIVE / DEACTIVE """
@importers.route('/active-deactive/<int:importer_id>', methods=['GET', 'POST'])
@login_required
def importer_active_deactive(importer_id):
    flash('Importer activado correctamente!')
    return redirect(url_for('importers.importers_index'))

""" FILTRO TIPOS """
@importers.route('/tipo', methods=['GET'])
@login_required
def importer_tipo_sorteo():
    tipo_sorteo = request.args.get('tipo_sorteo', default = '')
    page = int(request.args.get('page', 1))
    importers = Importer.get_tipo_sorteo(tipo_sorteo, page, current_app.config['ITEMS_PER_PAGE'])
    return render_template('importers.html',seccion="importers", importers=importers, tipos_sorteo=tipos_sorteo)

""" DELETE """
@importers.route('/delete/<int:importer_id>', methods=['GET', 'POST'])
@login_required
def importer_delete(importer_id):
    importer = Importer.get_by_id(importer_id)
    importer.delete()
    flash('Importer borrado correctamente!')
    return redirect(url_for('importers.importers_index'))


'''
    Comando para importar sorteos
    flask importers import
    flask importers import tipo_sorteo
'''
@importers.cli.command('import')
@click.argument('tipo_sorteo', required=False)
def importing(tipo_sorteo=None):
    current_app.logger.debug("Start Importing............")

    importing = ImportingSorteos()

    #con argumento importamos un tipo de sorteo especifico
    if tipo_sorteo is not None:
        print(tipo_sorteo)
    # sin argumento importamos todos
    else:
        importing.importingAll()

    current_app.logger.debug("Done Importing............")