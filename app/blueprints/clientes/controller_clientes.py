from flask import Blueprint,render_template, request, current_app, url_for
#from flask_login import login_required
from .model_cliente import Cliente

BP_NM = 'clientes'

clientes = Blueprint(BP_NM, __name__, template_folder='templates')
 
@clientes.route('/')
#@login_required
def clientes_index():
    
    page = int(request.args.get('page', 1))
    
    clientes = Cliente.all_paginated(page, current_app.config['ITEMS_PER_PAGE'])

    return render_template('clientes.html', clientes=clientes, seccion="clientes")

@clientes.route('/new')
#@login_required
def clientes_new():

    return render_template('clientes_new.html', clientes=clientes, seccion="clientes")

@clientes.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@clientes.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500