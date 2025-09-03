# 📌 Resume Cleaner (NLP Automation)

A lightweight Python script that automates resume parsing to extract skills, years of experience, and tech stack mentions.

---

## 🔹 Challenge
Recruiters spend hours manually scanning resumes, which is time-consuming and error-prone.

---

## 🔹 Approach
- Python script using Regex and keyword lists.
- Input: raw resume text (no PDF dependency required)
- Output: JSON/CSV with:
  - Core skills (Python, TensorFlow, Kubernetes, etc.)
  - Years of professional experience
  - Tech stack mentions

---

## 🔹 Usage
```bash
python resume_cleaner.py sample_resume.txt
