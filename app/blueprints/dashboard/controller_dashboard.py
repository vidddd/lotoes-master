from flask import Blueprint,render_template,current_app
from flask_mail import Message
from app import mail
from app.common.mail import send_email
#from flask_login import login_required

BP_NM = 'dashboard'

dashboard = Blueprint(BP_NM, __name__, template_folder='templates')
 
@dashboard.route('/')
#@login_required
def dashboard_func():
   
    send_email(subject='Holaaa',
                       sender=current_app.config['MAIL_FROM'],
                       recipients=[current_app.config['MAIL_SEND']],
                       text_body=f'Hola estas es dashboard',
                       html_body=f'Hola estas es dashboard')

    return render_template('dashboard.html', seccion="dashboard")

@dashboard.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')