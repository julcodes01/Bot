def generate_daily_report(jobs, date):
    subject = f"Daily Job Alert - {date}"

    if not jobs:
        body = "No IT/DevOps jobs matching your criteria were found today."
        return subject, body

    body = []
    body.append(f"IT & DevOps Jobs for {date}")
    body.append("=" * 50)
    body.append("")

    for index, job in enumerate(jobs, start=1):
        body.append(f"{index}. {job['title']}")
        body.append(f"Company: {job['company']}")
        body.append(f"Source: {job['source']}")
        body.append(f"Link: {job['link']}")
        body.append("-" * 50)

    body.append("")
    body.append(f"Total jobs found today: {len(jobs)}")
    body.append("")
    body.append("This report was generated automatically by your Job Alert Bot.")

    return subject, "\n".join(body)
