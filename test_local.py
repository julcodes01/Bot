"""
Local test script for Job Alert Bot
This allows you to test the bot locally without using GitHub Actions
"""
import os
from datetime import datetime, timezone
from jobs.remotive import get_remotive_jobs
from jobs.rss import get_rss_jobs


def test_fetch_jobs():
    """Test fetching jobs from all sources"""
    print("=" * 60)
    print("TESTING JOB ALERT BOT")
    print("=" * 60)
    print()

    # Test Remotive API
    print("1. Testing Remotive API...")
    try:
        remotive_jobs = get_remotive_jobs()
        print(f"   ✓ Found {len(remotive_jobs)} Remotive jobs")
        if remotive_jobs:
            print(f"   Sample: {remotive_jobs[0]['title']} at {remotive_jobs[0]['company']}")
    except Exception as e:
        print(f"   ✗ Error: {e}")

    print()

    # Test RSS Feeds
    print("2. Testing RSS Feeds...")
    try:
        rss_jobs = get_rss_jobs()
        print(f"   ✓ Found {len(rss_jobs)} RSS jobs")
        if rss_jobs:
            print(f"   Sample: {rss_jobs[0]['title']} at {rss_jobs[0]['company']}")
    except Exception as e:
        print(f"   ✗ Error: {e}")

    print()

    # Test filtering
    print("3. Testing entry-level filter...")
    all_jobs = []
    try:
        all_jobs.extend(remotive_jobs)
        all_jobs.extend(rss_jobs)
    except:
        pass

    keywords = ["junior", "entry", "intern", "associate", "trainee", "graduate"]
    filtered_jobs = [job for job in all_jobs if any(kw in job["title"].lower() for kw in keywords)]
    
    print(f"   ✓ Total jobs found: {len(all_jobs)}")
    print(f"   ✓ Entry-level jobs: {len(filtered_jobs)}")

    print()

    # Display some entry-level jobs
    if filtered_jobs:
        print("4. Sample Entry-Level Jobs:")
        print("-" * 60)
        for i, job in enumerate(filtered_jobs[:5], 1):
            print(f"   {i}. {job['title']}")
            print(f"      Company: {job['company']}")
            print(f"      Source: {job['source']}")
            print(f"      Link: {job['link'][:50]}...")
            print()
    else:
        print("4. No entry-level jobs found today")

    print()
    print("=" * 60)
    print("TEST COMPLETED")
    print("=" * 60)


def test_email_config():
    """Test email configuration"""
    print("\n5. Testing Email Configuration...")
    smtp_email = os.getenv("SMTP_EMAIL")
    smtp_password = os.getenv("SMTP_PASSWORD")
    
    if smtp_email and smtp_password:
        print(f"   ✓ SMTP_EMAIL configured: {smtp_email}")
        print(f"   ✓ SMTP_PASSWORD configured: {'*' * len(smtp_password)}")
    else:
        print("   ✗ SMTP credentials NOT configured")
        print("   Note: This is expected for local testing without env vars")
        print("   The workflow will use GitHub Secrets")
    print()


if __name__ == "__main__":
    test_fetch_jobs()
    test_email_config()
