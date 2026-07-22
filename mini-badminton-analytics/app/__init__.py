import os
import matplotlib
matplotlib.use('Agg')
from flask import Flask

def create_app():

    app = Flask(__name__)

    app.config.from_object("config.Config")

    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("data/processed", exist_ok=True)
    os.makedirs(app.config["PLOT_FOLDER"], exist_ok=True)

    from app.routes import main

    app.register_blueprint(main)

    return app