from .tournament import (
    plot_top_winners,
    plot_tournament_distribution,
    plot_duration_histogram,
    plot_score_difference
)

from .geography import (
    plot_city_distribution,
    plot_stadium_distribution
)


def generate_all_plots(df):

    plots = []

    plots.append(
        plot_top_winners(df)
    )

    plots.append(
        plot_tournament_distribution(df)
    )

    plots.append(
        plot_duration_histogram(df)
    )

    plots.append(
        plot_score_difference(df)
    )

    plots.append(
        plot_city_distribution(df)
    )

    plots.append(
        plot_stadium_distribution(df)
    )

    return plots