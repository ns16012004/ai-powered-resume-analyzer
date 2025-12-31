from flask import Blueprint, render_template, request, jsonify
from .resume_parser import parse_resume, analyze_resume
from datetime import datetime
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Define Blueprint
main = Blueprint('main', __name__)

# Inject current time into templates
@main.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

# Landing page (original HTML)
@main.route('/')
def home():
    return render_template('index.html')

# Original file upload route (HTML form)
@main.route('/upload', methods=['POST'])
def upload():
    if 'resume' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['resume']
    text = parse_resume(file)
    analysis = analyze_resume(text)
    return jsonify(analysis)

# -----------------------------
# API route for legacy JSON (React could use it if sending text)
# -----------------------------
@main.route("/api/analyze", methods=["POST", "GET"])
def analyze_api():
    if request.method == "GET":
        return jsonify({
            "message": "API is working. Send POST request with resume_text and job_description."
        })

    data = request.get_json()
    resume_text = data.get("resume_text", "")
    job_description = data.get("job_description", "")

    # TF-IDF similarity
    documents = [resume_text, job_description]
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(documents)
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    match_score = round(similarity * 100, 2)

    # Missing skills
    job_keywords = set([word.lower() for word in job_description.split()])
    resume_keywords = set([word.lower() for word in resume_text.split()])
    missing_skills = list(job_keywords - resume_keywords)

    return jsonify({
        "match_score": match_score,
        "missing_skills": missing_skills
    })

# -----------------------------
# NEW React-friendly route for file uploads
# -----------------------------
@main.route("/analyze", methods=["POST"])
def analyze_resume_api():
    if 'resume' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['resume']

    # Extract text using your existing parser
    text = parse_resume(file)

    # Analyze resume using your existing function
    analysis = analyze_resume(text)  # should return dict like {"score":..., "matched_skills":..., "missing_skills":...}

    return jsonify(analysis)
