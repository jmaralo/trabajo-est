# Description: Filter the data with the topics of the repository

import pandas as pd
import os

OUTPUT_DIR = "preprocessing/output"
OUTPUT_NAME = os.path.basename(__file__).replace(".py", ".csv")

TARGET_TOPICS = ["machine-learning", "api", "database", "android", "security"]


def filter_topics(t):
    for topic in TARGET_TOPICS:
        if topic in t:
            return topic
    return ""


def main(file="preprocessing/output/7_filter_lang.csv"):
    data = pd.read_csv(file, low_memory=False)

    data["topic"] = data["topics"].apply(filter_topics)
    data.drop(columns=["topics"], inplace=True)

    data = data.loc[data["topic"] != ""]

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    data.to_csv(os.path.join(OUTPUT_DIR, OUTPUT_NAME), index=False)


if __name__ == "__main__":
    main()
