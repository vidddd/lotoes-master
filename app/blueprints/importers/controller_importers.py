from flask import Blueprint, render_template, redirect, request, current_app, url_for, flash
import click
from .model_importer import Importer
#from flask_login import login_required

BP_NM = 'importers'

importers = Blueprint(BP_NM, __name__, template_folder='templates')
 
@importers.route('/')
#@login_required
def importers_index():
    
    page = int(request.args.get('page', 1))
    importers = Importer.all_paginated(page, current_app.config['ITEMS_PER_PAGE'])
    return render_template('importers.html', importers=importers)

'''
    Comando para importar sorteos
    flask importers import
    flask importers import tipo_sorteo
'''
@importers.cli.command('import')
@click.argument('tipo_sorteo', required=False)
def importing(tipo_sorteo=None):
    #con argumento importamos un tipo de sorteo especifico
    if tipo_sorteo is not None:
        print(tipo_sorteo)
    # sin argumento importamos todos
    else:
        print('importando todos')