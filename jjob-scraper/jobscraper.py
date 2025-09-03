"""
Job Postings Scraper (Market Skills Analysis)
Author: Asha Vittal

This script:
- Scrapes Indeed job postings
- Extracts job title, company, location, and summary
- Detects in-demand skills
- Outputs CSV + skill frequency bar chart
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import re

BASE_URL = "https://www.indeed.com/jobs?q=machine+learning+engineer&l=San+Francisco%2C+CA"

skills_list = [
    "Python", "TensorFlow", "PyTorch", "Kubernetes", "AWS",
    "Azure", "SQL", "Scikit-learn", "C++", "Java"
]

def extract_skills(text):
    """Find skills mentioned in job description text"""
    return [skill for skill in skills_list if skill.lower() in text.lower()]

def scrape_jobs(url):
    """Scrape Indeed job postings"""
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    jobs = []
    for job in soup.find_all("div", class_="job_seen_beacon"):
        title = job.find("h2").text.strip() if job.find("h2") else "N/A"
        company = job.find("span", class_="companyName")
        company = company.text.strip() if company else "N/A"
        location = job.find("div", class_="companyLocation")
        location = location.text.strip() if location else "N/A"
        summary = job.find("div", class_="job-snippet")
        summary = summary.text.strip() if summary else ""

        skills = extract_skills(summary)

        jobs.append({
            "Title": title,
            "Company": company,
            "Location": location,
            "Summary": summary,
            "Skills": skills
        })
    return jobs

def main():
    jobs = scrape_jobs(BASE_URL)
    df = pd.DataFrame(jobs)

    # Save to CSV
    df.to_csv("job_postings.csv", index=False)

    # Flatten skill list for counting
    all_skills = [s for sublist in df["Skills"] for s in sublist]
    skill_counts = pd.Series(all_skills).value_counts()

    # Plot
    skill_counts.plot(kind="bar", figsize=(10,5))
    plt.title("Top Skills in ML Engineer Job Postings")
    plt.ylabel("Frequency")
    plt.xlabel("Skill")
    plt.tight_layout()
    plt.savefig("skills_chart.png")

    print("✅ Job scraping complete! Results saved to job_postings.csv & skills_chart.png")


if __name__ == "__main__":
    main()
