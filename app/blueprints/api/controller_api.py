from flask import Blueprint, render_template, redirect, request, current_app, url_for, flash
#from flask_login import login_required

BP_NM = 'api'

api = Blueprint(BP_NM, __name__, template_folder='templates')
 
@api.route('/')
#@login_required
def api_index():
    
    page = int(request.args.get('page', 1))
    clientes = Cliente.all_paginated(page, current_app.config['ITEMS_PER_PAGE'])
    return render_template('clientes.html')
