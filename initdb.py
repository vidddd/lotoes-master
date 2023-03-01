#!/usr/bin/python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import app as application

#if env is None or env not in ["test", "prod"]:
env = "dev"

app = application.create_app(env)

from app import db

with app.app_context():
    db.drop_all()
    db.create_all()