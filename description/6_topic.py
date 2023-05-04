import pandas as pd


def main(variable="topic"):
    data = pd.read_csv("data/sample.csv")

    freq = pd.DataFrame({"absolute": data[variable].value_counts()})
    freq["relative"] = freq["absolute"] / len(data[variable])
    freq["accumulated"] = freq["absolute"].cumsum()
    freq["relative_accumulated"] = freq["relative"].cumsum()

    print(freq)


if __name__ == "__main__":
    main()
