# Description: Remove empty rows from the original dataset

import pandas as pd
import os

OUTPUT_DIR = "preprocessing/output"
OUTPUT_NAME = os.path.basename(__file__).replace(".py", ".csv")


def main(file="data/original.csv"):
    data = pd.read_csv(file, low_memory=False)

    data = data.loc[data["repo_link"].notna()]

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    data.to_csv(os.path.join(OUTPUT_DIR, OUTPUT_NAME), index=False)


if __name__ == "__main__":
    main()
