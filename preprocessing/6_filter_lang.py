# Description: Filter the data with the language of the repository

import pandas as pd
import os

OUTPUT_DIR = "preprocessing/output"
OUTPUT_NAME = os.path.basename(__file__).replace(".py", ".csv")

TARGET_LANGS = ["JavaScript", "Python", "Java", "C++"]


def main(file="preprocessing/output/5_with_topics.csv"):
    data = pd.read_csv(file, low_memory=False)

    data = data.loc[data["lang"].isin(TARGET_LANGS)]

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    data.to_csv(os.path.join(OUTPUT_DIR, OUTPUT_NAME), index=False)


if __name__ == "__main__":
    main()
