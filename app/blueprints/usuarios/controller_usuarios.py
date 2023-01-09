from flask import Blueprint,render_template, request, current_app, url_for
#from flask_login import login_required
from .model_usuario import Usuario

BP_NM = 'usuarios'

usuarios = Blueprint(BP_NM, __name__, template_folder='templates')
 
@usuarios.route('/')
#@login_required
def usuarios_index():
    
    #page = int(request.args.get('page', 1))
    
    #usuarios = Sorteo.all_paginated(page, current_app.con ig['ITEMS_PER_PAGE'])

    #return render_template('usuarios.html', usuarios=usuarios, seccion="usuarios")
    return render_template('usuarios.html')

@usuarios.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@usuarios.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500