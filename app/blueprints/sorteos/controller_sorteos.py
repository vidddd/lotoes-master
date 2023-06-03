from flask import Blueprint,render_template, request, current_app, url_for, Response
#from flask_login import login_required
from .model_sorteo import Sorteo
from config.lotoes_config import tipos_sorteo_game_id
from pprint import pprint
from inspect import getmembers

BP_NM = 'sorteos'

sorteos = Blueprint(BP_NM, __name__, template_folder='templates')
 
@sorteos.route('/')
#@login_required
def sorteos_index():
    page = int(request.args.get('page', 1))
    sorteos = Sorteo.all_paginated(page, current_app.config['ITEMS_PER_PAGE'])
    return render_template('sorteos.html', sorteos=sorteos, seccion="sorteos", tipos_sorteo=tipos_sorteo_game_id)

""" FILTRO TIPOS """
@sorteos.route('/tipo', methods=['GET'])
def sorteo_tipo_sorteo():
    tipo_sorteo = request.args.get('tipo_sorteo', default = '')
    page = int(request.args.get('page', 1))
    sorteos = Sorteo.get_tipo_sorteo(tipo_sorteo, page, current_app.config['ITEMS_PER_PAGE'])
    return render_template('sorteos.html', sorteos=sorteos, tipos_sorteo=tipos_sorteo_game_id)


@sorteos.route('/sorteo/<int:sorteo_id>')
#@login_required
def sorteo(sorteo_id):
    sorteo = Sorteo.get_by_id(sorteo_id)
    pprint(getmembers(sorteo.primitiva_combinacion))
    if sorteo is None:
        raise NotFound(sorteo_id)
    return render_template('sorteo.html', debug=True, sorteo=sorteo, seccion='sorteos')

def dpm(variable):
    pp = pprint.PrettyPrinter(indent=4, depth=6)
    debug_message = pp.pprint(variable)
    return Response(debug_message, mimetype="text/text")