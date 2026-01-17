"""
Test email configuration without actually sending
"""
import os
from jobs.rss import get_rss_jobs
from jobs.remotive import get_remotive_jobs
from report.daily import generate_daily_report
from datetime import datetime, timezone


def test_email_flow():
    print("=" * 60)
    print("TESTING EMAIL FLOW")
    print("=" * 60)
    print()
    
    # Step 1: Check environment variables
    print("1. Checking SMTP Configuration...")
    smtp_email = os.getenv("SMTP_EMAIL")
    smtp_password = os.getenv("SMTP_PASSWORD")
    
    if smtp_email and smtp_password:
        print(f"   ✓ SMTP_EMAIL: {smtp_email}")
        print(f"   ✓ SMTP_PASSWORD: {'*' * 16} (configured)")
    else:
        print("   ✗ SMTP credentials NOT set in environment")
        print("   Note: This is expected locally. GitHub Actions uses secrets.")
    print()
    
    # Step 2: Fetch jobs
    print("2. Fetching jobs...")
    all_jobs = []
    
    try:
        rss_jobs = get_rss_jobs()
        all_jobs.extend(rss_jobs)
        print(f"   ✓ RSS Jobs: {len(rss_jobs)}")
    except Exception as e:
        print(f"   ✗ RSS Error: {e}")
    
    try:
        remotive_jobs = get_remotive_jobs()
        all_jobs.extend(remotive_jobs)
        print(f"   ✓ Remotive Jobs: {len(remotive_jobs)}")
    except Exception as e:
        print(f"   ✗ Remotive Error: {e}")
    
    print(f"   Total jobs fetched: {len(all_jobs)}")
    print()
    
    # Step 3: Filter jobs
    print("3. Filtering jobs...")
    keywords = ["junior", "entry", "intern", "associate", "trainee", "graduate",
                "developer", "engineer", "devops", "sre", "cloud", "backend",
                "frontend", "full stack", "fullstack", "web developer", "software"]
    
    filtered_jobs = [job for job in all_jobs if any(kw in job['title'].lower() for kw in keywords)]
    print(f"   ✓ Matching jobs: {len(filtered_jobs)}")
    print()
    
    # Step 4: Generate email content
    print("4. Generating email content...")
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    
    if filtered_jobs:
        subject, body = generate_daily_report(filtered_jobs, today)
        print(f"   ✓ Subject: {subject}")
        print(f"   ✓ Body length: {len(body)} characters")
        print()
        print("=" * 60)
        print("EMAIL PREVIEW:")
        print("=" * 60)
        print(f"Subject: {subject}")
        print()
        print(body[:500])  # Show first 500 chars
        if len(body) > 500:
            print(f"\n... (truncated, total {len(body)} chars)")
    else:
        print("   ✗ No jobs to report")
    
    print()
    print("=" * 60)
    
    # Step 5: Check Gmail App Password requirements
    print("\n5. Gmail Configuration Checklist:")
    print("   □ 2-Factor Authentication enabled on Google Account")
    print("   □ App Password generated (not regular Gmail password)")
    print("   □ App Password is 16 characters (no spaces)")
    print("   □ SMTP_EMAIL matches the Gmail account")
    print("   □ GitHub Secrets are correctly named:")
    print("     - SMTP_EMAIL")
    print("     - SMTP_PASSWORD")
    print()


if __name__ == "__main__":
    test_email_flow()
