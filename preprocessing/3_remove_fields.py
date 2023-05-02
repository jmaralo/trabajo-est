# Description: Remove unnecessary fields from the data

import pandas as pd
import os

OUTPUT_DIR = "preprocessing/output"
OUTPUT_NAME = os.path.basename(__file__).replace(".py", ".csv")

data = pd.read_csv(
    "preprocessing/output/2_clean_lang.csv", low_memory=False)


data = data.drop(columns=["repo_name", "repo_about",
                 "repo_webs", "license", "author"])

os.makedirs(OUTPUT_DIR, exist_ok=True)
data.to_csv(os.path.join(OUTPUT_DIR, OUTPUT_NAME), index=False)
