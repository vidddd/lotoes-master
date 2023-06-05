from flask import Blueprint,render_template, request, current_app, url_for
from flask_login import login_required
from .model_usuario import Usuario
from .form_usuarios import LoginForm

BP_NM = 'usuarios'

usuarios = Blueprint(BP_NM, __name__, template_folder='templates')

@usuarios.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('dashboard'))
        print('Invalid username or password.')
        flash('Invalid username or password.')
    return render_template('login.html', form=form)

@usuarios.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
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
