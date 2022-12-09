import os

import app as application

application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lotoesmaster:Madridejos.6677@localhost/lotoesmaster'

application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(application)


env = os.getenv('FLASK_CONFIG')
#if env is None or env not in ["test", "prod"]:
env = "dev"

app = application.create_app(env)
