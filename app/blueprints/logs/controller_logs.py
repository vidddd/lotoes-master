import os
from flask import Blueprint,render_template,current_app
from flask_mail import Message
from app import mail, db
from app.common.mail import send_email
from flask_login import login_required
from app.blueprints.usuarios.model_usuario import Usuario

BP_NM = 'logs'

logs = Blueprint(BP_NM, __name__, template_folder='templates')
 
@logs.route('/')
@login_required
def logs_func():
    with open('logs/lotoes-master.log') as f:
        logs = [row.rstrip('\n') for row in f]
        logs.sort(reverse=True)
    return render_template('logs.html', logs=logs, seccion="logs")

@logs.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
