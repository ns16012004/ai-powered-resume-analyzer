import os
from pdfminer.high_level import extract_text
from io import BytesIO
from dotenv import load_dotenv
import json
import time
import re  # Needed for cleaning JSON content

# Import openai
try:
    import openai
except ImportError:
    print("Failed to import openai module")

# Load environment variables from .env file
load_dotenv()

# Get API key
api_key = os.getenv('OPENAI_API_KEY')
if api_key:
    print(f"Loaded API key: {api_key[:10]}...")

# Set API key for openai
if 'openai' in globals():
    openai.api_key = api_key

# Check OpenAI version
is_new_version = False
try:
    import pkg_resources
    openai_version = pkg_resources.get_distribution("openai").version
    is_new_version = int(openai_version.split('.')[0]) >= 1
    print(f"OpenAI version: {openai_version}")
except Exception:
    is_new_version = False

# Initialize client
client = None
try:
    if is_new_version:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        print("Initialized OpenAI client with new API")
    else:
        print("Using old OpenAI API")
except Exception as e:
    print("Error initializing OpenAI client:", e)
    is_new_version = False

# ----------- Functions ------------

def parse_resume(file):
    """Extract text from PDF resume"""
    file_content = file.read()
    pdf_file = BytesIO(file_content)
    text = extract_text(pdf_file)
    return text


def analyze_resume(resume_text):
    """Analyze resume using OpenAI and return JSON feedback"""
    global is_new_version, client, openai

    max_retries = 3
    retry_delay = 2

    try:
        prompt = f"""Analyze this resume and provide detailed feedback in JSON format:
{{
    "atsScore": {{
        "score": 85,
        "scoreBreakdown": {{
            "keywords": 20,
            "formatting": 15,
            "experience": 25,
            "skills": 15,
            "education": 10
        }},
        "improvements": ["Specific suggestions to improve ATS score"]
    }},
    "feedback": {{
        "overallAssessment": {{
            "strengths": ["list of key strengths"],
            "areasForImprovement": ["list of areas to improve"]
        }},
        "educationSection": {{
            "strengths": ["list of strengths"],
            "areasForImprovement": ["list of improvements"]
        }},
        "extraCurricularActivities": {{
            "strengths": ["list of strengths"],
            "areasForImprovement": ["list of improvements"]
        }},
        "awardsAndAchievements": {{
            "strengths": ["list of strengths"],
            "areasForImprovement": ["list of improvements"]
        }},
        "professionalExperience": {{
            "strengths": ["list of strengths"],
            "areasForImprovement": ["list of improvements"]
        }},
        "aboutMeSection": {{
            "strengths": ["list of strengths"],
            "areasForImprovement": ["list of improvements"]
        }},
        "skillsSection": {{
            "strengths": ["list of strengths"],
            "areasForImprovement": ["list of improvements"]
        }}
    }}
}}

Resume text:
{resume_text}

Provide an ATS score out of 100 and specific feedback for each section.
Ensure JSON is properly formatted.
"""

        messages = [
            {"role": "system", "content": "You are a professional resume reviewer. Provide feedback in JSON."},
            {"role": "user", "content": prompt}
        ]

        content = None
        last_error = None

        for attempt in range(max_retries):
            try:
                use_old_api = False

                if is_new_version and client is not None:
                    try:
                        print(f"Attempt {attempt+1}/{max_retries}: Using new OpenAI API...")
                        response = client.chat.completions.create(
                            model="gpt-4o-mini",
                            messages=messages,
                            temperature=0.7,
                            max_tokens=2000
                        )
                        content = response.choices[0].message.content.strip()
                        break
                    except Exception as new_api_error:
                        error_message = str(new_api_error)
                        print(f"New API error: {error_message}")
                        use_old_api = True
                else:
                    use_old_api = True

                if use_old_api:
                    response = openai.ChatCompletion.create(
                        model="gpt-4o-mini",
                        messages=messages,
                        temperature=0.7,
                        max_tokens=2000
                    )
                    content = response['choices'][0]['message']['content'].strip()
                    break

            except Exception as loop_error:
                last_error = loop_error
                print(f"Retry {attempt+1} failed: {loop_error}")
                time.sleep(retry_delay)

        if content is None:
            return {"error": f"Failed after {max_retries} attempts", "last_error": str(last_error)}

        # Clean code fences if present
        cleaned_content = re.sub(r"```json|```", "", content).strip()

        try:
            feedback = json.loads(cleaned_content)
            return feedback
        except json.JSONDecodeError:
            print("JSON parsing failed")
            return {"error": "Invalid JSON returned by OpenAI", "raw_content": content}

    except Exception as e:
        print("Fatal error in analyze_resume:", e)
        return {"error": str(e)}
