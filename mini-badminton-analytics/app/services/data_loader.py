import pandas as pd
from flask import current_app


def load_data():

    path = current_app.config["RAW_DATA"]

    df = pd.read_excel(path)

    return df