"""
Resume Cleaner (NLP Automation)
Author: Asha Vittal

This script extracts:
- Skills
- Years of experience
- Tech stack mentions

Input: Raw resume text file
Output: JSON + console printout
"""

import re
import json
import sys

# ✅ Define a sample skills list (expand as needed)
skills_list = [
    "Python", "TensorFlow", "PyTorch", "Kubernetes", "AWS",
    "Azure", "Java", "C++", "SQL", "Spark", "Hadoop", "Scikit-learn"
]

def extract_skills(text):
    """Return a list of skills found in resume text"""
    return [skill for skill in skills_list if skill.lower() in text.lower()]

def extract_experience(text):
    """Return max years of experience found in resume text"""
    matches = re.findall(r'(\d+)\+?\s+years', text.lower())
    return max([int(m) for m in matches], default=0)

def main(file_path):
    with open(file_path, "r") as f:
        resume_text = f.read()

    skills_found = extract_skills(resume_text)
    experience_years = extract_experience(resume_text)

    output = {
        "skills": skills_found,
        "years_experience": experience_years
    }

    # Save to JSON
    with open("resume_output.json", "w") as out:
        json.dump(output, out, indent=4)

    print("✅ Resume parsed successfully!")
    print(json.dumps(output, indent=4))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python resume_cleaner.py sample_resume.txt")
    else:
        main(sys.argv[1])
