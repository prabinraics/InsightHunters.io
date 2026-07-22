import pandas as pd


def dataset_summary(df):

    summary = {

        "rows": df.shape[0],

        "columns": df.shape[1],

        "missing_values": int(
            df.isnull().sum().sum()
        ),

        "duplicate_rows": int(
            df.duplicated().sum()
        )

    }

    return summary


def numerical_summary(df):

    return df.describe().round(2)


def top_winners(df):

    return (
        df["winner"]
        .value_counts()
        .head(10)
    )


def top_cities(df):

    return (
        df["city"]
        .value_counts()
        .head(10)
    )


def tournament_distribution(df):

    return (
        df["tournament"]
        .value_counts()
    )


def stadium_distribution(df):

    return (
        df["stadium"]
        .value_counts()
    )