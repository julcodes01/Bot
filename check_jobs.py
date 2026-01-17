from jobs.rss import get_rss_jobs

jobs = get_rss_jobs()
print(f'Total jobs fetched: {len(jobs)}')
print("\nFirst 10 job titles:")
print("=" * 80)

for i, job in enumerate(jobs[:10], 1):
    print(f"{i}. {job['title']}")

print("\n" + "=" * 80)

# Check for entry-level keywords
keywords = ["junior", "entry", "intern", "associate", "trainee", "graduate", 
            "developer", "engineer", "devops", "sre", "cloud", "backend", 
            "frontend", "full stack", "fullstack", "web developer", "software"]
entry_level = [job for job in jobs if any(kw in job['title'].lower() for kw in keywords)]

print(f"\nMatching jobs found: {len(entry_level)}")
if entry_level:
    print("\nMatching job titles:")
    for i, job in enumerate(entry_level, 1):
        print(f"{i}. {job['title']}")
else:
    print("\nNo jobs with the expanded keywords found")
