import os
from flask import Blueprint,render_template,current_app
from flask_mail import Message
from app import mail, db
from app.common.mail import send_email
from flask_login import login_required
from app.blueprints.usuarios.model_usuario import Usuario

BP_NM = 'dashboard'

dashboard = Blueprint(BP_NM, __name__, template_folder='templates')
 
@dashboard.route('/')
@login_required
def dashboard_func():
    ''' send_email(subject='Holaaa',
                       sender=current_app.config['LOTOES_MAIL_FROM'],
                       recipients=[current_app.config['LOTOES_MAIL_SEND']],
                       text_body=f'Hola estas es dashboard',
                       html_body=f'Hola estas es dashboard')
                       '''
    #current_app.logger.info("Index page loading")

    return render_template('dashboard.html', seccion="dashboard")

@dashboard.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

'''
    Comando inicializar la base de datos
'''
@dashboard.cli.command('init-db')
def init_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
    print('init db')
    
@dashboard.cli.command('create-suuser')
def create_suuser():
    username=os.getenv('LOTOES_USER', default='')
    email = os.getenv('LOTOES_EMAIL', default='')
    password = os.getenv('LOTOES_PASSWORD', default='')
    new_user = Usuario(id=None, username=username, password=password, email=email, is_admin=True)
    db.session.add(new_user)
    db.session.commit()
    print('user created.')
