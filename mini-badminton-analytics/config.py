import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "badminton_secret"

    RAW_DATA = os.path.join(
        BASE_DIR,
        "data",
        "raw",
        "badminton_matches_cleaned.xlsx"
    )

    PROCESSED_DATA = os.path.join(
        BASE_DIR,
        "data",
        "processed",
        "badminton_processed.xlsx"
    )

    PLOT_FOLDER = os.path.join(
        BASE_DIR,
        "app",
        "static",
        "images",
        "plots"
    )