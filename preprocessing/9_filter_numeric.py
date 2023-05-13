# Description: Drop unwanted columns and apply type conversion

import pandas as pd
import os

OUTPUT_DIR = "preprocessing/output"
OUTPUT_NAME = os.path.basename(__file__).replace(".py", ".csv")


def main(file="preprocessing/output/7_filter_topics.csv", keep=["lang", "topic", "commits_count", "contrib_count", "issue_count", "stars_count"], numerics=["commits_count", "contrib_count", "issue_count", "stars_count"]):
    data = pd.read_csv(file, low_memory=False)

    data = data[keep]

    for numeric in numerics:
        data[numeric] = data[numeric].astype(int)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    data.to_csv(os.path.join(OUTPUT_DIR, OUTPUT_NAME), index=False)


if __name__ == "__main__":
    main()
