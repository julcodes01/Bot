import requests


def get_remotive_jobs() -> list[dict[str, str]]:
    url = "https://remotive.io/api/remote-jobs"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"Warning: Could not fetch Remotive jobs: {e}")
        return []

    jobs: list[dict[str, str]] = []

    for job in data.get("jobs", []):
        title = job.get("title", "")
        company = job.get("company_name", "")
        link = job.get("url", "")
        category = job.get("category", "")

        # Focus on IT related categories
        if any(x in category.lower() for x in ["software", "it", "devops", "cloud", "engineering"]):
            jobs.append({
                "title": title,
                "company": company,
                "link": link,
                "source": "Remotive"
            })

    return jobs
