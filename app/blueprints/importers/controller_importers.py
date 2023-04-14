from flask import Blueprint, render_template, redirect, request, current_app, url_for, flash
import click
#from flask_login import login_required

BP_NM = 'importers'

importers = Blueprint(BP_NM, __name__, template_folder='templates')
 
@importers.route('/')
#@login_required
def importers_index():
    
    #page = int(request.args.get('page', 1))
    #clientes = Cliente.all_paginated(page, current_app.config['ITEMS_PER_PAGE'])
    return render_template('importers.html')

@importers.cli.command('import')
@click.argument('tipo_sorteo')
def importing(tipo_sorteo):
    print('importing')
    print(tipo_sorteo)
