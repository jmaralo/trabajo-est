# Description: Remove duplicate rows from the data

import pandas as pd
import os

OUTPUT_DIR = "preprocessing/output"
OUTPUT_NAME = os.path.basename(__file__).replace(".py", ".csv")


def main(file="preprocessing/output/0_remove_empty.csv"):
    data = pd.read_csv(file, low_memory=False)

    data = data.drop_duplicates(subset=["repo_link"])

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    data.to_csv(os.path.join(OUTPUT_DIR, OUTPUT_NAME), index=False)


if __name__ == "__main__":
    main()
