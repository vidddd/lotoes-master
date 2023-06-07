from flask import Blueprint,render_template, request, current_app, url_for, flash, redirect
from flask_login import login_required, login_user, logout_user
from .model_usuario import Usuario
from .form_usuarios import LoginForm
from app import db
from werkzeug.security import check_password_hash

BP_NM = 'usuarios'

usuarios = Blueprint(BP_NM, __name__, template_folder='templates')

@usuarios.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():   
        email = form.email.data
        password = form.password.data
        remember_me = True if form.remember_me.data else False
        usuario = Usuario.query.filter_by(email=email).first()

        #if not usuario or not usuario.check_password(password):
        if not usuario:
            flash('Please check your login details and try again.')
            return render_template('login.html', form=form)

        login_user(usuario)
        usuario.ping_last_login()
        return redirect(request.args.get('next') or url_for('dashboard.dashboard_func'))
    else:
        return render_template('login.html', form=form)
        
@usuarios.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('usuarios.login'))

@usuarios.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    username='david'
    email = ''
    password = ''
    new_user = Usuario(id=None, username=username, password=generate_password_hash(password), email=email, is_admin=True)
    db.session.add(new_user)
    db.session.commit()
    flash('user created.')
    return redirect(url_for('usuarios.login'))


@usuarios.route('/')
@login_required
def usuarios_index():
    page = int(request.args.get('page', 1))
    usuarios = Usuario.all_paginated(page, current_app.config['ITEMS_PER_PAGE'])
    return render_template('usuarios.html', usuarios=usuarios, seccion="usuarios")


@usuarios.route('/usuario/<int:usuario_id>')
@login_required
def usuario(usuario_id):
    usuario = Usuario.get_by_id(usuario_id)
    if usuario is None:
        raise NotFound(usuario_id)
    return render_template('usuario.html', debug=True, usuario=usuario, seccion='usuarios')
