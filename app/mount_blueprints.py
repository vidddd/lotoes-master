
def mount_blueprints(app, config_name):
    if not app:
        return
    
    from app.blueprints.dashboard import dashboard
    from app.blueprints.sorteos import sorteos
    from app.blueprints.usuarios import usuarios
    from app.blueprints.clientes import clientes
    from app.blueprints.administraciones import administraciones

    app.register_blueprint(dashboard, url_prefix='')
    app.register_blueprint(sorteos, url_prefix='/sorteos')
    app.register_blueprint(usuarios, url_prefix='/usuarios')
    app.register_blueprint(clientes, url_prefix='/clientes')
    app.register_blueprint(administraciones, url_prefix='/administraciones')
