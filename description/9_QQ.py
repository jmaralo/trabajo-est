from math import ceil, sqrt
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

SMALL_SIZE = 25
MEDIUM_SIZE = 30
BIGGER_SIZE = 35


def main(variables=["commits_count", "contrib_count", "issue_count", "stars_count"]):
    plt.rc('font', size=SMALL_SIZE)
    plt.rc('axes', titlesize=BIGGER_SIZE)
    plt.rc('xtick', labelsize=SMALL_SIZE)
    plt.rc('ytick', labelsize=SMALL_SIZE)
    plt.rc('legend', fontsize=SMALL_SIZE)

    plt.style.use("seaborn-darkgrid")

    data = pd.read_csv("data/sample.csv")

    rows = ceil(sqrt(len(variables)))
    cols = ceil(sqrt(len(variables)))
    _, axes = plt.subplots(rows, cols)

    for i, variable in enumerate(variables):
        ax = axes[i // cols][i % cols]
        stats.probplot(data[variable], dist="norm", plot=ax)
        ax.set_title("Grafico Q-Q " + variable)
        ax.set_xlabel("")
        ax.set_ylabel("")

    plt.show()


if __name__ == "__main__":
    main()
