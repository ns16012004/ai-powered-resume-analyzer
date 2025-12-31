import requests
import os
from pdfminer.high_level import extract_text

# === Step 1: Set your resume path ===
resume_path = r"C:\Users\nihar\ai-powered-resume-analyzer\resume.pdf.pdf"

# Check if file exists
if not os.path.exists(resume_path):
    print(f"Error: {resume_path} does not exist!")
    exit(1)

# === Step 2: Extract text from PDF ===
try:
    resume_text = extract_text(resume_path)
    if not resume_text.strip():
        print("Warning: PDF text is empty!")
except Exception as e:
    print("Error extracting text from PDF:", e)
    exit(1)

# === Step 3: Prepare data for API ===
data = {
    "resume_text": resume_text,
    "job_description": "Looking for Python developer with ML and SQL skills"
}

# === Step 4: Send POST request to backend API ===
url = "http://127.0.0.1:5000/api/analyze"

try:
    response = requests.post(url, json=data)
    # Print response in readable format
    print("API Response:")
    print(response.json())
except Exception as e:
    print("Error calling API:", e)
