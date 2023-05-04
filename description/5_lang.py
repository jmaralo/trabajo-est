import pandas as pd
import matplotlib.pyplot as plt

SMALL_SIZE = 25
MEDIUM_SIZE = 30
BIGGER_SIZE = 35

plt.rc('font', size=SMALL_SIZE)
plt.rc('axes', titlesize=BIGGER_SIZE)
plt.rc('xtick', labelsize=SMALL_SIZE)
plt.rc('ytick', labelsize=SMALL_SIZE)
plt.rc('legend', fontsize=SMALL_SIZE)

plt.style.use("seaborn-darkgrid")


def main(variable="lang"):
    data = pd.read_csv("data/sample.csv")

    data[variable].value_counts().plot(kind="bar")
    plt.show()

    data[variable].value_counts().plot(kind="pie", xlabel="", ylabel="")
    plt.show()


if __name__ == "__main__":
    main()
