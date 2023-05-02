# Description: Parse the language field and extract the most used language

import json
import pandas as pd
import os

OUTPUT_DIR = "preprocessing/output"
OUTPUT_NAME = os.path.basename(__file__).replace(".py", ".csv")

data = pd.read_csv(
    "preprocessing/output/1_remove_duplicates.csv", low_memory=False)


def parse_lang(langs):
    try:
        langs = langs.replace("Cap'n Proto", "Capn Proto")
        langs = langs.replace("Ren'Py", "RenPy")
        langs = langs.replace("'", '"')
        langs_dict = json.loads(langs)
        if not langs_dict:
            return ""

        for lang in langs_dict:
            langs_dict[lang] = float(langs_dict[lang].replace("%", ""))
        return max(langs_dict, key=langs_dict.get)
    except Exception as e:
        print("Error parsing {langs} ({err})".format(langs=langs, err=e))
        raise e


data["lang"] = data["langs"].apply(parse_lang)
data = data.drop(columns=["langs"])
data = data.loc[data["lang"] != ""]

os.makedirs(OUTPUT_DIR, exist_ok=True)
data.to_csv(os.path.join(OUTPUT_DIR, OUTPUT_NAME), index=False)
