import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

from .helper import save_figure
from .helper import get_plot_metadata


def plot_top_winners(df):

    winners = (
        df["winner"]
        .value_counts()
        .head(10)
    )

    fig = plt.figure(figsize=(10,5))

    sns.barplot(
        x=winners.values,
        y=winners.index
    )

    plt.title("Top 10 Winners")

    filename = save_figure(
        fig,
        "top_winners.png"
    )

    return get_plot_metadata(
        "Top Winners",
        filename,
        "Top winning players or teams."
    )


def plot_tournament_distribution(df):

    tournaments = (
        df["tournament"]
        .value_counts()
    )

    fig = plt.figure(figsize=(8,8))

    plt.pie(
        tournaments.values,
        labels=tournaments.index,
        autopct="%1.1f%%"
    )

    plt.title("Tournament Distribution")

    filename = save_figure(
        fig,
        "tournament_distribution.png"
    )

    return get_plot_metadata(
        "Tournament Distribution",
        filename,
        "Distribution of matches by tournament."
    )


def plot_duration_histogram(df):

    fig = plt.figure(figsize=(8,5))

    sns.histplot(
        df["duration_minutes"],
        bins=15
    )

    plt.title("Match Duration")

    filename = save_figure(
        fig,
        "duration_histogram.png"
    )

    return get_plot_metadata(
        "Duration Histogram",
        filename,
        "Distribution of match duration."
    )


def plot_score_difference(df):

    fig = plt.figure(figsize=(8,5))

    sns.histplot(
        df["ScoreDifference"],
        bins=15
    )

    plt.title("Score Difference")

    filename = save_figure(
        fig,
        "score_difference.png"
    )

    return get_plot_metadata(
        "Score Difference",
        filename,
        "Difference between home and away score."
    )