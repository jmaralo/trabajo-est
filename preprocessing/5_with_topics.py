# Description: Fetch topics for repos (this takes a long time due to the GitHub API rate limit)
# A valid GitHub API token must be provided in the TOKEN variable

import pandas as pd
import requests
import os
import time

TOKEN = "<<-- YOUR GITHUB TOKEN HERE -->>"
OUTPUT_DIR = "preprocessing/output"
OUTPUT_NAME = os.path.basename(__file__).replace(".py", ".csv")

data = pd.read_csv("preprocessing/4_output/4_expand_numbers.csv")


def get_topics(repo):
    print("Getting topics for {repo}".format(repo=repo))
    try:
        while True:
            parts = repo.split("/")
            req = requests.get("https://api.github.com/repos/{owner}/{name}".format(owner=parts[-2], name=parts[-1]), headers={
                "Accept": "application/vnd.github+json", "Authorization": "Bearer {token}".format(token=TOKEN), "X-GitHub-Api-Version": "2022-11-28"})

            info = req.json()
            if "topics" in info:
                return req.json()["topics"]

            if "message" in info and (info["message"] == "Not Found" or info["message"] == "Repository access blocked"):
                return []

            time.sleep(60 * 10)
    except Exception as e:
        print("Error getting topics for {repo} ({err})".format(
            repo=repo, err=e))
        return []


data["topics"] = data["repo_link"].apply(get_topics)

os.makedirs(OUTPUT_DIR, exist_ok=True)
data.to_csv(os.path.join(OUTPUT_DIR, OUTPUT_NAME), index=False)
