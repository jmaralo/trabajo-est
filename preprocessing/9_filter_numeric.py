# Description: Drop unwanted columns and apply type conversion

import pandas as pd
import os

OUTPUT_DIR = "preprocessing/output"
OUTPUT_NAME = os.path.basename(__file__).replace(".py", ".csv")

data = pd.read_csv("preprocessing/output/8_sample.csv", low_memory=False)

data = data[["lang", "topic", "commits_count",
             "contrib_count", "issue_count", "stars_count"]]

data["commits_count"] = data["commits_count"].astype(int)
data["contrib_count"] = data["contrib_count"].astype(int)
data["issue_count"] = data["issue_count"].astype(int)
data["stars_count"] = data["stars_count"].astype(int)

os.makedirs(OUTPUT_DIR, exist_ok=True)
data.to_csv(os.path.join(OUTPUT_DIR, OUTPUT_NAME), index=False)
