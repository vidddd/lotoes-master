from flask import Blueprint,render_template
from flask_login import login_required

BP_NM = 'dashboard'

dashboard = Blueprint(BP_NM, __name__, template_folder='templates')
 
@dashboard.route('/')
#@login_required
def dashboard_func():
    return render_template('dashboard.html', seccion="dashboard")

@dashboard.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')