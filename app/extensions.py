import logging
from flask import render_template

def register_error_handlers(app):

    @app.errorhandler(500)
    def base_error_handler(e):
        return render_template('500.html'), 500

    @app.errorhandler(404)
    def error_404_handler(e):
        return render_template('404.html'), 404

    @app.errorhandler(401)
    def error_401_handler(e):
        return render_template('401.html'), 401
    
def configure_logging(app):
    # Elimina los manejadores por defecto de la app
    del app.logger.handlers[:]
    loggers = [app.logger, ]
    handlers = []
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(verbose_formatter())
    
    if (app.config['APP_ENV'] == 'dev') or (
            app.config['APP_ENV'] == 'test') or (
            app.config['APP_ENV'] == 'prod'):
        console_handler.setLevel(logging.DEBUG)
        handlers.append(console_handler)
    elif app.config['APP_ENV'] == 'prod':
        console_handler.setLevel(logging.INFO)
        handlers.append(console_handler)
    for l in loggers:
        for handler in handlers:
            l.addHandler(handler)
        l.propagate = False
        l.setLevel(logging.DEBUG)
        
def verbose_formatter():
    return logging.Formatter(
        '[%(asctime)s.%(msecs)d]\t %(levelname)s \t[%(name)s.%(funcName)s:%(lineno)d]\t %(message)s',
        datefmt='%d/%m/%Y %H:%M:%S'
    )