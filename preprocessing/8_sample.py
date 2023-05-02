# Description: Create a sample from the data

import pandas as pd
import os

OUTPUT_DIR = "preprocessing/output"
OUTPUT_NAME = os.path.basename(__file__).replace(".py", ".csv")

N = 900

data = pd.read_csv(
    "preprocessing/output/7_filter_topics.csv", low_memory=False)

data = data.sample(n=N)

os.makedirs(OUTPUT_DIR, exist_ok=True)
data.to_csv(os.path.join(OUTPUT_DIR, OUTPUT_NAME), index=False)
