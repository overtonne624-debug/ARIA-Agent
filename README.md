# 🤖 ARIA — Autonomous Research & Intelligence Agent

> An autonomous multi-agent AI platform that transforms raw datasets into machine learning insights, explainable results, critical evaluation, and executive-ready reports.
>
> ## 🚀 Live Demo

👉 **[Try ARIA Live](https://aria-agent-seven.vercel.app/)**

> Explore the deployed ARIA interface and project workflow.

> **Demo note:** The screenshots below showcase ARIA's completed analysis workflow using a sample dataset. The live deployment is provided as a project interface demonstration.
>
> ## 🎥 Project Demo

> 🎬 Demo video coming soon — a complete walkthrough of ARIA's autonomous data-science workflow.


![ARIA](https://img.shields.io/badge/ARIA-Autonomous%20AI-blue)
![Python](https://img.shields.io/badge/Python-3.10+-yellow)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![React](https://img.shields.io/badge/React-Frontend-61DAFB)
![Machine Learning](https://img.shields.io/badge/ML-Automated-orange)
![License](https://img.shields.io/badge/License-MIT-purple)

## 🚀 Overview

ARIA (Autonomous Research & Intelligence Agent) is a multi-agent AI system designed to automate the end-to-end data science workflow.

Instead of manually exploring datasets, selecting machine learning models, generating explanations, checking model reliability, and preparing reports, ARIA coordinates multiple specialized agents to perform these tasks automatically.

### The goal

**Upload a dataset → ARIA analyzes it → explains the results → evaluates reliability → generates a report.**

---

## 🖥️ ARIA in Action

### 1. Analysis Summary
![ARIA Analysis Summary](images/01_analysis_summary.jpg)

### 2. Results Overview
![ARIA Results Overview](images/02_result_overview.jpg)

### 3. System Health
![ARIA System Health](images/03_system_health.jpg)

### 4. Insights & Recommendations
![ARIA Insights and Recommendations](images/04_insights_recommendations.jpg)

### 5. SHAP Explainability
![ARIA SHAP Explainability](images/05_shap_explainability.jpg)

### 6. SHAP Details
![ARIA SHAP Details](images/06_shap_details.jpg)


*ARIA's web interface showing automated multi-agent dataset analysis.*

## 🧠 What ARIA Does

ARIA automates the core stages of a data science workflow through specialized AI agents.

**1. 📊 Understands Data**  
Examines dataset structure, dimensions, data types, and potential data-quality issues.

**2. 🤖 Performs Analysis**  
Automatically performs machine learning analysis and evaluates suitable models.

**3. 🔍 Explains Results**  
Uses explainability techniques such as SHAP to identify influential features.

**4. 🛡️ Critically Evaluates Results**  
Checks the analysis for potential risks, limitations, and reliability concerns.

**5. 📝 Generates Reports**  
Converts the analysis into understandable insights, recommendations, visualizations, and reports.

## ✨ Key Features

- 📊 Automated dataset understanding
- 🤖 Automated machine learning model selection
- 📈 Classification and regression analysis
- 🔍 Feature importance and explainability
- 🧠 Multi-agent AI workflow
- 🛡️ Critical evaluation of model results
- 📝 Automated executive-style reports
- 📉 Automatic chart generation
- 💾 Persistent agent memory
- 🌐 Web-based interface
- 📄 PDF report generation

---

## 🧩 Multi-Agent Architecture

ARIA uses specialized agents for different stages of the data science workflow.

| Agent | Responsibility |
|---|---|
| 📊 Data Agent | Understands and preprocesses the dataset |
| 🧮 Analysis Agent | Selects and evaluates machine learning models |
| 🔍 Explainability Agent | Identifies important features and explains predictions |
| 🛡️ Critic Agent | Checks reliability, risks and potential issues |
| 📝 Report Agent | Converts results into an executive-ready report |

Additional research and memory components support the overall workflow.

---

## 🔄 How ARIA Works

```text
                ┌─────────────────┐
                │ Upload Data │
                └────────┬────────┘
                         ↓
                ┌─────────────────┐
                │ Data Agent │
                └────────┬────────┘
                         ↓
                ┌─────────────────┐
                │ Analysis Agent │
                └────────┬────────┘
                         ↓
              ┌──────────┴──────────┐
              ↓ ↓
      Explainability Agent Critic Agent
              │ │
              └──────────┬──────────┘
                         ↓
                ┌─────────────────┐
                │ Report Agent │
                └────────┬────────┘
                         ↓
                ┌─────────────────┐
                │ Insights + PDF │
                └─────────────────┘
