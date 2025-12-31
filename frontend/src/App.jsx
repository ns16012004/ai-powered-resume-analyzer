import { useState } from "react";

function App() {
  const [resumeText, setResumeText] = useState("");
  const [jobDesc, setJobDesc] = useState("");
  const [result, setResult] = useState(null);

  const handleAnalyze = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch("http://127.0.0.1:5000/api/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ resume_text: resumeText, job_description: jobDesc }),
      });

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setResult({ error: "Failed to connect to backend" });
    }
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h1>AI Resume Analyzer</h1>
      <form onSubmit={handleAnalyze}>
        <textarea
          placeholder="Paste your resume text"
          value={resumeText}
          onChange={(e) => setResumeText(e.target.value)}
          rows={6}
          style={{ width: "100%", marginBottom: "1rem" }}
        />
        <textarea
          placeholder="Paste job description"
          value={jobDesc}
          onChange={(e) => setJobDesc(e.target.value)}
          rows={4}
          style={{ width: "100%", marginBottom: "1rem" }}
        />
        <button type="submit">Analyze Resume</button>
      </form>

      {result && (
        <div style={{ marginTop: "2rem" }}>
          {result.error ? (
            <p style={{ color: "red" }}>{result.error}</p>
          ) : (
            <>
              <p><strong>Match Score:</strong> {result.match_score}</p>
              <p><strong>Missing Skills:</strong> {result.missing_skills.join(", ")}</p>
            </>
          )}
        </div>
      )}
    </div>
  );
}

export default App;
