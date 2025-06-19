from flask import Flask
from .extensions import db
from .models import Hero, Power, HeroPower
from .routes import routes  
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    app.register_blueprint(routes)

    return app
