import pandas as pd


def main(variable1="lang", variable2="topic"):
    data = pd.read_csv("data/sample.csv")

    absolute = pd.crosstab(data[variable1], data[variable2], margins=True)
    print("absolute:")
    print(absolute)

    print()

    print("relative:")
    print(absolute / len(data[variable1]))


if __name__ == "__main__":
    main()
