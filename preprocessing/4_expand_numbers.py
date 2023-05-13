# Description: Expand numeric fields

import pandas as pd
import os

OUTPUT_DIR = "preprocessing/output"
OUTPUT_NAME = os.path.basename(__file__).replace(".py", ".csv")


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


def main(file="preprocessing/output/3_remove_fields.csv", numerics=["issue_count", "pulls_count", "fork_count", "stars_count", "branch_count", "tags_count", "commits_count", "contrib_count"]):
    data = pd.read_csv(file, low_memory=False)

    for numeric in numerics:
        data[numeric] = data[numeric].apply(parse_number)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    data.to_csv(os.path.join(OUTPUT_DIR, OUTPUT_NAME), index=False)


if __name__ == "__main__":
    main()
