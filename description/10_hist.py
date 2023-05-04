from math import ceil, sqrt
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

SMALL_SIZE = 25
MEDIUM_SIZE = 30
BIGGER_SIZE = 35

plt.rc('font', size=SMALL_SIZE)
plt.rc('axes', titlesize=BIGGER_SIZE)
plt.rc('xtick', labelsize=SMALL_SIZE)
plt.rc('ytick', labelsize=SMALL_SIZE)
plt.rc('legend', fontsize=SMALL_SIZE)

plt.style.use("seaborn-darkgrid")


def main(variables=["commits_count", "contrib_count", "issue_count", "stars_count"], units=["commits", "contributors", "issues", "stars"], bins=50):
    data = pd.read_csv("data/sample.csv")

    rows = ceil(sqrt(len(variables)))
    cols = ceil(sqrt(len(variables)))
    _, axes = plt.subplots(rows, cols)

    for i, variable in enumerate(variables):
        ax = axes[i // cols][i % cols]

        data[variable].hist(ax=ax, bins=bins)
        ax.set_xlim(data[variable].min(), data[variable].max())
        ax.set_title("Histograma " + variable)
        ax.set_xlabel(units[i])
        ax.set_ylabel("Frecuencia")

    plt.show()


if __name__ == "__main__":
    main()