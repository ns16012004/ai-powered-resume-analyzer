# AI-Powered Resume Analyzer with ATS Scoring

![AI Resume Analyzer](https://img.shields.io/badge/Resume%20Analyzer-AI%20Powered-blue)
![ATS Scoring](https://img.shields.io/badge/ATS%20Score-0--100-green)
![Flask](https://img.shields.io/badge/Flask-Python-red)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-lightgrey)

A **modern web application** that leverages AI to analyze resumes and provide **ATS compatibility scores** with detailed, actionable feedback to help job seekers optimize their CVs and pass automated screening systems.

---

## 🚀 Features

### 🎯 ATS Compatibility Scoring
- **Score (0-100)**: Evaluate your resume against common Applicant Tracking Systems.
- **Score Breakdown**:
  - **Keywords (0-25)**: Are industry-specific keywords included?  
  - **Formatting (0-20)**: Clean, ATS-readable layout.  
  - **Experience (0-25)**: Clear job titles, companies, dates, and achievements.  
  - **Skills (0-20)**: Relevant technical and soft skills highlighted.  
  - **Education (0-10)**: Properly listed degrees and institutions.  

### 🤖 AI-Powered Feedback
- **Strengths & Areas to Improve**: Section-by-section analysis.  
- **Professional Recommendations**: Specific steps to improve your resume.  
- **Industry Standard Insights**: Align your resume with current hiring trends.

### 💻 User Experience
- **Upload PDF resumes** directly on the web interface.  
- **Fast analysis** with live progress indicators.  
- **Clean, responsive UI**: Works on desktop and mobile devices.  
- **Error handling**: Alerts if resume upload or processing fails.  

---

## 💻 Technologies Used

### Backend
- Python 3.9+  
- Flask 3.0.2 for REST APIs and web app framework  
- OpenAI GPT-4 for AI-powered resume analysis  
- PDFMiner for extracting text from PDF resumes  

### Frontend
- React 19 for modern, responsive user interfaces  
- HTML5 & CSS3 with responsive layouts  
- Vite as a fast frontend build tool  

### Deployment
- Render for cloud deployment  
- Gunicorn for production-ready Flask server  
- Environment Variables to securely store OpenAI API keys  

---

## 📋 How It Works

1. **Upload Your Resume**  
   - Upload PDF file safely for instant processing.

2. **AI Analysis Engine**  
   - Resume is parsed, and AI generates a comprehensive ATS score.  
   - Strengths and improvement areas identified.

3. **Detailed Results**  
   - **ATS Score** (0-100) with visual breakdown.  
   - Section-wise feedback: Education, Experience, Skills, Achievements, etc.  
   - Actionable tips for improvements.

---

## 🔧 Local Setup

### Prerequisites
- Python 3.9+
- Node.js 20.19+ (for frontend)
- OpenAI API key

### Steps
```bash
# Clone the repository
git clone https://github.com/<your-username>/ai-powered-resume-analyzer.git
cd ai-powered-resume-analyzer

# Backend setup
python -m venv venv
# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file with your OpenAI API key
echo "OPENAI_API_KEY=your_api_key_here" > .env

# Run backend
python run.py

# Frontend setup
cd frontend
npm install
npm run dev

ai-powered-resume-analyzer/
│
├── app/                    # Flask backend
│   ├── __init__.py         # App initialization
│   ├── routes.py           # API endpoints
│   ├── resume_parser.py    # PDF parsing and AI analysis
│   ├── static/             # CSS & JS files
│   └── templates/          # Jinja2 templates
├── frontend/               # React frontend
│   ├── src/                # React components & assets
│   ├── public/             # Public files
│   └── package.json        # Frontend dependencies
├── venv/                   # Python virtual environment (ignored)
├── .gitignore              # Ignore sensitive & build files
├── run.py                  # Backend entry point
├── test_api.py             # Test backend APIs
├── requirements.txt        # Backend dependencies
└── README.md               # Project documentation

📝 License

This project is licensed under the MIT License – see the LICENSE
 file.

👩‍💻 Author

Niharika – https://github.com/ns16012004


