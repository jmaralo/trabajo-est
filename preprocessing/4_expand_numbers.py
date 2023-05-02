# Description: Expand numeric fields

import pandas as pd
import os

OUTPUT_DIR = "preprocessing/output"
OUTPUT_NAME = os.path.basename(__file__).replace(".py", ".csv")

data = pd.read_csv(
    "preprocessing/output/3_remove_fields.csv", low_memory=False)


def parse_number(number):
    try:
        if type(number) != str:
            return int(number)

        if number == "∞":
            return float("inf")

        number = number.replace("+", "")

        if number.endswith("m"):
            number = number.replace("m", "")
        elif number.endswith("k"):
            number = number.replace("k", "")

        return float(number)
    except Exception as e:
        print("Error parsing {number} ({err})".format(number=number, err=e))
        raise e


data["issue_count"] = data["issue_count"].apply(parse_number)
data["pulls_count"] = data["pulls_count"].apply(parse_number)
data["fork_count"] = data["fork_count"].apply(parse_number)
data["stars_count"] = data["stars_count"].apply(parse_number)
data["branch_count"] = data["branch_count"].apply(parse_number)
data["tags_count"] = data["tags_count"].apply(parse_number)
data["commits_count"] = data["commits_count"].apply(parse_number)
data["contrib_count"] = data["contrib_count"].apply(parse_number)

os.makedirs(OUTPUT_DIR, exist_ok=True)
data.to_csv(os.path.join(OUTPUT_DIR, OUTPUT_NAME), index=False)
