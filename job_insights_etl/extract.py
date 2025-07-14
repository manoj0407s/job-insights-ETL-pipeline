import os
import requests
from dotenv import load_dotenv

load_dotenv()

def extract_jobs(pages=3):
    app_id = os.getenv("ADZUNA_APP_ID")
    app_key = os.getenv("ADZUNA_API_KEY")
    all_results = []

    for page in range(1, pages + 1):
        url = f"https://api.adzuna.com/v1/api/jobs/in/search/{page}?app_id={app_id}&app_key={app_key}&results_per_page=10"
        response = requests.get(url)
        response.raise_for_status()
        all_results.extend(response.json()["results"])

    return all_results
