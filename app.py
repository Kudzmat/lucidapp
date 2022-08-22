from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# instantiate application and database
app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lucid_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# create login manager
# login_manager = LoginManager()
# login_manager.init_app(app)

import routes, models
