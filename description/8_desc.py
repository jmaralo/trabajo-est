import pandas as pd


def main(variables=["commits_count", "contrib_count", "issue_count", "stars_count"]):
    data = pd.read_csv("data/sample.csv")

    table = pd.DataFrame(columns=[
                         "mean", "median", "std", "variance", "var_coef", "rang", "q_rang", "skew", "kurt"])
    for variable in variables:
        mean = data[variable].mean()
        median = data[variable].median()
        std = data[variable].std()
        variance = std ** 2
        var_coef = std / mean
        rang = data[variable].max() - data[variable].min()
        q_rang = data[variable].quantile(0.75) - data[variable].quantile(0.25)
        skew = data[variable].skew()
        kurt = data[variable].kurt()

        row = [mean, median, std, variance, var_coef, rang, q_rang, skew, kurt]
        table.loc[variable] = row

    print(table)


if __name__ == "__main__":
    main()
