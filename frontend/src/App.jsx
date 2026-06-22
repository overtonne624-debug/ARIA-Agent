import "./App.css";
import { useState } from "react";


function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const handleAnalyze = async () => {
    if (!file) {
      alert("Please select a CSV file");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://127.0.0.1:8000/upload", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      console.log(data);
      setResult(data);
    } catch (error) {
      console.error(error);
      alert("Backend connection failed");
    }
  };

  return (
    <div className="App">
      <h1>🤖 ARIA Dashboard</h1>

      <h3>Autonomous Research & Intelligence Agent</h3>

      <hr />

      <div style={{ marginTop: "20px" }}>
        <h2>Dataset Upload</h2>

        <input type="file" onChange={(e) => setFile(e.target.files[0])} />

        <br />
        <br />

        <button onClick={handleAnalyze}>Analyze Dataset</button>
      </div>

      <div className="card">
  <h2>Agent Status</h2>

  <ul className="status-box">
          <li>✅ Data Agent</li>
          <li>✅ Analysis Agent</li>
          <li>✅ Explainability Agent</li>
          <li>✅ Critic Agent</li>
          <li>✅ Report Agent</li>
        </ul>
      </div>

      <div style={{ marginTop: "30px" }}>
        <h2>Results</h2>

        {result ? (
  <div className="card">
            <div className="section-card">

  <h3>Dataset Summary</h3>

  <p>Rows: {result.summary.rows}</p>

  <p>Columns: {result.summary.columns}</p>

</div>

           <div className="section-card">

  <h3>Research Summary</h3>

  <p>{result.research_summary}</p>

</div>
<div className="section-card">

  <h3>Narrative Report</h3>

  <pre
    style={{
      whiteSpace: "pre-wrap",
      textAlign: "left",
      padding: "10px",
      backgroundColor: "#f5f5f5"
    }}
  >
    {result.narrative_report}
  </pre>

</div>

<div className="section-card">

  <h3>Insights</h3>

  <p>{result.insights}</p>

</div>
<div className="section-card">

  <h3>Recommendations</h3>

  <p>{result.recommendations}</p>

</div>
<div className="section-card">

  <h3>Conclusion</h3>

  <p>{result.conclusion}</p>

</div>
<div className="section-card">
<h3>Downloads</h3>

<a
  href="http://127.0.0.1:8000/reports/analysis_report.pdf"
  target="_blank"
>
  📄 Download PDF Report
</a>
</div>

<br /><br />

<a
  href="http://127.0.0.1:8000/reports/chart.png"
  target="_blank"
>
  📈 Download Chart
</a>
<div className="section-card">
<h3>SHAP Explainability</h3>

<img
  src="http://127.0.0.1:8000/reports/shap_summary.png"
  alt="SHAP Summary"
  style={{
    width: "100%",
    maxWidth: "900px",
    marginTop: "10px"
  }}
/>
</div>
<br /><br />

<a
  href="http://127.0.0.1:8000/reports/shap_summary.png"
  target="_blank"
>
  📊 Download SHAP Report
</a>

            <h3>Question Answer</h3>

            <p>{result.question_answer}</p>
          </div>
        ) : (
          <p>
            Upload a dataset and click Analyze Dataset to generate insights.
          </p>
        )}
      </div>
    </div>
  );
}

export default App;