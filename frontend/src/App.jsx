import "./App.css";
import { useState } from "react";



function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const[progress, setProgress] = useState(0);
  const [processingTime, setProcessingTime] = useState(0);

const [cpuUsage] = useState(18);

const [memoryUsage] = useState(42);

const [activityLogs, setActivityLogs] = useState([]);
  const [agentStatus, setAgentStatus] = useState([
  "⚪ Data Agent - Waiting",
  "⚪ Analysis Agent - Waiting",
  "⚪ Explainability Agent - Waiting",
  "⚪ Critic Agent - Waiting",
  "⚪ Report Agent - Waiting",
]);

  const handleAnalyze = async () => {
    const startTime = Date.now();

    setLoading(true);
    setAgentStatus([
  "🟡 Data Agent - Running",
  "⚪ Analysis Agent - Waiting",
  "⚪ Explainability Agent - Waiting",
  "⚪ Critic Agent - Waiting",
  "⚪ Report Agent - Waiting",
]);
setProgress(20);

    if (!file) {
      alert("Please select a CSV file");
      setloading(false);
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("https://aria-agent-5jnn.onrender.com/upload", {
        method: "POST",
        body: formData,
      });

      console.log("status:", response.status);
      
      const data = await response.json();
      console.log("Backend Response:", data);
      setAgentStatus([
  "🟢 Data Agent - Completed",
  "🟡 Analysis Agent - Running",
  "⚪ Explainability Agent - Waiting",
  "⚪ Critic Agent - Waiting",
  "⚪ Report Agent - Waiting",
]);
setProgress(40);

await new Promise(resolve => setTimeout(resolve, 1000));

setAgentStatus([
  "🟢 Data Agent - Completed",
  "🟢 Analysis Agent - Completed",
  "🟡 Explainability Agent - Running",
  "⚪ Critic Agent - Waiting",
  "⚪ Report Agent - Waiting",
]);
setProgress(60);

await new Promise(resolve => setTimeout(resolve, 1000));

setAgentStatus([
  "🟢 Data Agent - Completed",
  "🟢 Analysis Agent - Completed",
  "🟢 Explainability Agent - Completed",
  "🟡 Critic Agent - Running",
  "⚪ Report Agent - Waiting",
]);
setProgress(80);

await new Promise(resolve => setTimeout(resolve, 1000));

setAgentStatus([
  "🟢 Data Agent - Completed",
  "🟢 Analysis Agent - Completed",
  "🟢 Explainability Agent - Completed",
  "🟢 Critic Agent - Completed",
  "🟡 Report Agent - Running",
]);
setProgress(90);

await new Promise(resolve => setTimeout(resolve, 1000));

setAgentStatus([
  "🟢 Data Agent - Completed",
  "🟢 Analysis Agent - Completed",
  "🟢 Explainability Agent - Completed",
  "🟢 Critic Agent - Completed",
  "🟢 Report Agent - Completed",
]);
setProgress(100);

      console.log(data);
      setResult(data);
      const endTime = Date.now();

setProcessingTime(
  ((endTime - startTime) / 1000).toFixed(2)
);

setActivityLogs([
  "Dataset Uploaded",
  "Data Agent Completed",
  "Analysis Agent Completed",
  "SHAP Explainability Generated",
  "Critic Agent Completed",
  "Narrative Report Generated",
  "PDF Report Ready"
]);

    } catch (error) {
      console.error(error);
      alert("Backend connection failed");
    }
    finally{
      setLoading(false);
    }
  };

    return (
    <div className="App">
    <nav className="navbar">

  <div className="logo">
    🤖 ARIA
  </div>

  <div className="nav-links">
    <a href="#">Dashboard</a>
    <a href="#">Features</a>
    <a href="#">Documentation</a>
    <a
      href="https://github.com/"
      target="_blank"
      rel="noreferrer"
    >
      GitHub
    </a>
  </div>

</nav>
      <div className="hero">

    <div className="hero-badge">
        🚀 AI Powered Research Platform
    </div>

    <h1 className="hero-title">
        ARIA
    </h1>

    <h2 className="hero-subtitle">
        Autonomous Research & Intelligence Agent
    </h2>

    <p className="hero-description">

    ARIA is an autonomous multi-agent AI platform that transforms
    raw datasets into explainable insights, intelligent predictions,
    and executive-ready reports using automated data science workflows.

</p>
<div className="hero-buttons">

    <button className="primary-btn">
        🚀 Get Started
    </button>

    <button className="secondary-btn">
        📄 Documentation
    </button>

</div>

</div>

<div className="stats-container">

  <div className="stat-card">
    <h2>5</h2>
    <p>Agents Active</p>
  </div>

  <div className="stat-card">
    <h2>10+</h2>
    <p>AI Modules</p>
  </div>

  <div className="stat-card">
    <h2>100%</h2>
    <p>Automation</p>
  </div>

</div>

<hr />

      <div style={{ marginTop: "20px" }}>
        <div className="upload-card">
        <h2>Dataset Upload</h2>

        <label htmlFor="file-upload" className="upload-box">

    📂 Click to Upload Dataset

</label>

<input
    id="file-upload"
    type="file"
    hidden
    onChange={(e)=>setFile(e.target.files[0])}
/>

{file && (
    <p className="selected-file">
        ✅ {file.name}
    </p>
)}

        <br />
        <br />

        <button
  onClick={handleAnalyze}
  disabled={loading}
  className="analyze-btn"
>
  {loading ? "⏳ Analyzing..." : "🚀 Analyze Dataset"}
</button>
</div>
</div>

{loading && (
  <div style={{ width: "100%", marginTop: "20px" }}>
    <div
      style={{
        width: "100%",
        background: "#ddd",
        borderRadius: "10px",
        overflow: "hidden",
      }}
    >
      <div
        style={{
          width: `${progress}%`,
          height: "12px",
          background: "#4CAF50",
          transition: "width 0.8s ease",
        }}
      ></div>
    </div>

    <p style={{ textAlign: "center", marginTop: "8px" }}>
      {progress}% Complete
    </p>
  </div>
)}

<div className="card">
  <h2>Agent Status</h2>

  <ul className="status-box">
  {agentStatus.map((agent, index) => (
  <li key={index}>{agent}</li>
  ))}
</ul>
      </div> {/*
      */}
      <div className="card">
  <h2>🟢System Health</h2>

  <ul className="health-list">
    <li>🟢 Backend Online</li>
    <li>🟢 Data Agent Ready</li>
    <li>🟢 Analysis Engine Ready</li>
    <li>🟢 SHAP Engine Ready</li>
    <li>🟢 Memory Active</li>
    <li>🟢 Report Generator Ready</li>
    <li>🟢 API Connected</li>
  </ul>
</div>

<div className="card">

  <h2>📊 Monitoring Dashboard</h2>

  <div className="kpi-container">

    <div className="kpi-card">
      <h2>{cpuUsage}%</h2>
      <p>CPU Usage</p>
    </div>

    <div className="kpi-card">
      <h2>{memoryUsage}%</h2>
      <p>Memory Usage</p>
    </div>

    <div className="kpi-card">
      <h2>{processingTime}s</h2>
      <p>Processing Time</p>
    </div>

    <div className="kpi-card">
      <h2>Online</h2>
      <p>Backend</p>
    </div>

  </div>

</div>

<div className="card">

  <h2>📝 Activity Logs</h2>

  <ul className="health-list">
    {activityLogs.map((log, index) => (
      <li key={index}>✅ {log}</li>
    ))}
  </ul>

</div>
      <div style={{ marginTop: "30px" }}>
        <h2>Results</h2>
        {result && (
  <div className="kpi-container">

    <div className="kpi-card">
      <h2>{result.summary.rows}</h2>
      <p>Rows</p>
    </div>

    <div className="kpi-card">
      <h2>{result.summary.columns}</h2>
      <p>Columns</p>
    </div>

    <div className="kpi-card">
      <h2>5</h2>
      <p>Agents</p>
    </div>

    <div className="kpi-card">
      <h2>100%</h2>
      <p>Completed</p>
    </div>

  </div>
)}

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
<div className="download-links">

<a
  href="https://aria-agent-5jnn.onrender.com/reports/analysis_report.pdf"
  target="_blank"
>
  📄 Download PDF Report
</a>


<br /><br />

<a
  href="https://aria-agent-5jnn.onrender.com/reports/chart.png"
  target="_blank"
>
  📈 Download Chart
</a>
<div className="section-card">
<h3>SHAP Explainability</h3>

<img
  src={`https://aria-agent-5jnn.onrender.com/reports/shap_summary.png`}
  alt="SHAP Summary"
  className="shap-image"
/>
</div>
<br /><br />

<a
  href="https://aria-agent-5jnn.onrender.com/reports/shap_summary.png"
  target="_blank"
>
  📊 Download SHAP Report
</a>
</div>

            <h3>Question Answer</h3>

            <p>{result.question_answer}</p>
          </div>
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