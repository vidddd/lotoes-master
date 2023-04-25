from flask import Blueprint,render_template, request, current_app, url_for
#from flask_login import login_required
from .model_sorteo import Sorteo
from config.lotoes_config import tipos_sorteo

BP_NM = 'sorteos'

sorteos = Blueprint(BP_NM, __name__, template_folder='templates')
 
@sorteos.route('/')
#@login_required
def sorteos_index():
    
    page = int(request.args.get('page', 1))
    sorteos = Sorteo.all_paginated(page, current_app.config['ITEMS_PER_PAGE'])
    return render_template('sorteos.html', sorteos=sorteos, seccion="sorteos", tipos_sorteo=tipos_sorteo)