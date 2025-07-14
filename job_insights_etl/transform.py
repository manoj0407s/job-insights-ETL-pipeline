from datetime import datetime

def transform_jobs(raw_jobs):
    clean_jobs = []
    for job in raw_jobs:
        clean_jobs.append({
            "id": job.get("id"),
            "title": job.get("title", "").strip().title(),
            "company": job.get("company", {}).get("display_name", "").strip(),
            "location": job.get("location", {}).get("display_name", "").strip(),
            "description": job.get("description", "")[:1000],
            "date_posted": datetime.fromisoformat(job["created"].replace("Z", "")).date()
        })
    return clean_jobs
