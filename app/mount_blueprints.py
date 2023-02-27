
def mount_blueprints(app, config_name):
    if not app:
        return
    
    from app.blueprints.dashboard import dashboard
    from app.blueprints.sorteos import sorteos
    from app.blueprints.usuarios import usuarios

    app.register_blueprint(dashboard, url_prefix='')
    app.register_blueprint(sorteos, url_prefix='/sorteos')
    app.register_blueprint(usuarios, url_prefix='/usuarios')
