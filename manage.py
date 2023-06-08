#!/usr/bin/env python
import os

if os.path.exists('.env'):
    print('Importing environment from .env...')
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]

from app import create_app, db
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

user = os.getenv('LOTOES_USER')
email = os.getenv('LOTOES_EMAIL')
password = os.getenv('LOTOES_PASSWORD')

db.drop_all()
db.create_all()