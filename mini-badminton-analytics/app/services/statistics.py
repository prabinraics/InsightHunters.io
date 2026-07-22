import pandas as pd


def dashboard_statistics(df):

    stats = {

        "total_matches":

            len(df),

        "total_tournaments":

            df["tournament"].nunique(),

        "total_winners":

            df["winner"].nunique(),

        "total_cities":

            df["city"].nunique(),

        "total_stadiums":

            df["stadium"].nunique(),

        "average_duration":

            round(
                df["duration_minutes"].mean(),
                2
            ),

        "longest_match":

            int(
                df["duration_minutes"].max()
            ),

        "shortest_match":

            int(
                df["duration_minutes"].min()
            ),

        "highest_total_score":

            int(
                df["TotalScore"].max()
            ),

        "average_score":

            round(
                df["TotalScore"].mean(),
                2
            )

    }

    return stats


def winner_statistics(df):

    winners = (

        df.groupby("winner")

        .size()

        .reset_index(name="Wins")

        .sort_values(

            by="Wins",

            ascending=False

        )

    )

    return winners


def tournament_statistics(df):

    tournaments = (

        df.groupby("tournament")

        .agg(

            Matches=("tournament", "count"),

            AvgDuration=(

                "duration_minutes",

                "mean"

            )

        )

        .round(2)

    )
    

    return tournaments

def longest_matches(df):

    return (

        df.sort_values(

            "duration_minutes",

            ascending=False

        )

        .head(5)

    )