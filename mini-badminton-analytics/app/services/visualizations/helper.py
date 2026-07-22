import os
import matplotlib.pyplot as plt
from flask import current_app

def save_figure(fig, filename):

    folder = current_app.config["PLOT_FOLDER"]

    os.makedirs(folder, exist_ok=True)

    filepath = os.path.join(folder, filename)

    fig.savefig(filepath, dpi=300, bbox_inches="tight")

    plt.close(fig)

    return filename


def get_plot_metadata(title, filename, caption):

    return {
        "title": title,
        "filename": filename,
        "caption": caption
    }