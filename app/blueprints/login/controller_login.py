from flask import Blueprint,render_template
#from flask_login import login_required

BP_NM = 'login'

login = Blueprint(BP_NM, __name__, template_folder='templates')

@login.route('/login')
def login():
    return render_template('login.html')