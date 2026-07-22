from flask import Blueprint, render_template, request

from app.services.data_loader import load_data
from app.services.preprocessing import clean_data
from app.services.statistics import dashboard_statistics
from app.services.eda import dataset_summary
from app.services.visualizations.generate import generate_all_plots

from app.services.statistics import longest_matches
main = Blueprint("main", __name__)


@main.route("/")
def index():

    df = load_data()

    df = clean_data(df)
    
    top_longest = longest_matches(df)

    tournament = request.args.get("tournament")

    if tournament:

        df = df[df["tournament"] == tournament]

    stats = dashboard_statistics(df)

    summary = dataset_summary(df)

    plots = generate_all_plots(df)

    tournaments = sorted(
        df["tournament"].unique()
    )

    recent_matches = df.sort_values(
        "date",
        ascending=False
    ).head(10)

    return render_template(

        "index.html",

        stats=stats,

        summary=summary,

        plots=plots,

        tournaments=tournaments,

        recent_matches=recent_matches,
        
        top_longest=top_longest

    )
    