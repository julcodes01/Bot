from collections import Counter
from datetime import datetime, timezone


def generate_weekly_report(jobs):
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    subject = f"Weekly Job Report - {today}"

    if not jobs:
        body = "No IT/DevOps jobs matching your criteria were found during the past week."
        return subject, body

    total_jobs = len(jobs)

    companies = [job["company"] for job in jobs]
    titles = [job["title"] for job in jobs]
    sources = [job["source"] for job in jobs]

    top_companies = Counter(companies).most_common(5)
    common_titles = Counter(titles).most_common(5)
    source_count = Counter(sources)

    body = []
    body.append("WEEKLY JOB SUMMARY REPORT")
    body.append("=" * 50)
    body.append("")

    body.append(f"Report Date: {today}")
    body.append(f"Total Entry Level Jobs Found This Week: {total_jobs}")
    body.append("")

    body.append("Jobs by Source:")
    for source, count in source_count.items():
        body.append(f"- {source}: {count}")

    body.append("")
    body.append("Top Hiring Companies:")
    for company, count in top_companies:
        body.append(f"- {company}: {count} positions")

    body.append("")
    body.append("Most Common Job Titles:")
    for title, count in common_titles:
        body.append(f"- {title}: {count} times")

    body.append("")
    body.append("DETAILED JOB LIST")
    body.append("=" * 50)
    body.append("")

    for index, job in enumerate(jobs, start=1):
        body.append(f"{index}. {job['title']}")
        body.append(f"Company: {job['company']}")
        body.append(f"Source: {job['source']}")
        body.append(f"Link: {job['link']}")
        body.append("-" * 50)

    body.append("")
    body.append("This weekly report was generated automatically by your Job Alert Bot.")
    body.append("Keep pushing – your next opportunity is coming.")

    return subject, "\n".join(body)
