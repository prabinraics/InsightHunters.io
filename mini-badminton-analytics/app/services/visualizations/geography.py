import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

from .helper import save_figure
from .helper import get_plot_metadata


def plot_city_distribution(df):

    cities = (
        df["city"]
        .value_counts()
        .head(10)
    )

    fig = plt.figure(figsize=(10,5))

    sns.barplot(
        x=cities.values,
        y=cities.index
    )

    plt.title("Top Cities")

    filename = save_figure(
        fig,
        "top_cities.png"
    )

    return get_plot_metadata(
        "Top Cities",
        filename,
        "Cities hosting most matches."
    )


def plot_stadium_distribution(df):

    stadiums = (
        df["stadium"]
        .value_counts()
        .head(10)
    )

    fig = plt.figure(figsize=(10,5))

    sns.barplot(
        x=stadiums.values,
        y=stadiums.index
    )

    plt.title("Top Stadiums")

    filename = save_figure(
        fig,
        "top_stadiums.png"
    )

    return get_plot_metadata(
        "Top Stadiums",
        filename,
        "Most frequently used stadiums."
    )