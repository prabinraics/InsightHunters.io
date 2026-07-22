import pandas as pd
from flask import current_app


def clean_data(df):
    """
    Clean the badminton dataset
    """

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Convert date
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Clean text columns
    text_columns = [
        "stage",
        "stadium",
        "city",
        "home_team",
        "away_team",
        "winner",
        "tournament",
        "match_type",
        "category"
    ]

    for col in text_columns:
        if col in df.columns:
            df[col] = (
                df[col]
                .astype(str)
                .str.strip()
                .str.title()
            )

    # Fill numeric null values
    numeric = df.select_dtypes(include="number").columns

    for col in numeric:
        df[col] = df[col].fillna(df[col].median())

    # Fill object null values
    objects = df.select_dtypes(include="object").columns

    for col in objects:
        if df[col].isnull().sum() > 0:
            df[col] = df[col].fillna(df[col].mode()[0])

    # Feature Engineering
    if (
        "home_score" in df.columns and
        "away_score" in df.columns
    ):

        df["TotalScore"] = (
            df["home_score"] +
            df["away_score"]
        )

        df["ScoreDifference"] = (
            abs(
                df["home_score"] -
                df["away_score"]
            )
        )

    if "duration_minutes" in df.columns:
        df["DurationHours"] = (
            df["duration_minutes"] / 60
        )

    return df


def save_processed_data(df):

    path = current_app.config["PROCESSED_DATA"]

    df.to_excel(
        path,
        index=False
    )