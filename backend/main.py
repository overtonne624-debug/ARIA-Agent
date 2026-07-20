import json
import numpy as np
import pandas as pd
from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

from agents.memory_agent import store_memory, retrieve_memory
from agents.narrative_agent import generate_narrative
from agents.critic_agent import run_critic
from agents.analysis_agent import run_analysis
from agents.explainability_agent import get_feature_importance, generate_explanation, generate_shap_explanation
from agents.data_agent import analyze_dataset
from agents.research_agent import generate_research_summary
from agents.question_answering_agent import answer_question
from agents.insight_agent import generate_insights
from agents.data_profiler import profile_data
from agents.report_generator import generate_chart, generate_pdf
from tools.data_loader import load_csv


app = FastAPI(
    title="ARIA API",
    description="Autonomous Research & Intelligence Agent",
    version="1.0.0"
)
import os

os.makedirs("reports", exist_ok=True)

app.mount(
    "/reports",
    StaticFiles(directory="reports"),
    name="reports"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def sanitize(obj):
    if isinstance(obj, dict):
        return {k: sanitize(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [sanitize(i) for i in obj]
    elif isinstance(obj, np.integer):
        return int(obj)
    elif isinstance(obj, np.floating):
        return float(obj)
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    return obj


@app.get("/")
def home():
    return {"message": "ARIA Backend Running"}


@app.post("/upload")
async def upload_dataset(file: UploadFile = File(...)):

    save_path = f"datasets/{file.filename}"

    with open(save_path, "wb") as buffer:
        buffer.write(await file.read())

    summary = load_csv(save_path)

    df = pd.read_csv(save_path)
    data_analysis = analyze_dataset(df)

    analysis_result = run_analysis(
        df,
        data_analysis["possible_target"]
    )

    model_object = analysis_result.get("model_object")

    feature_importance = analysis_result.get(
        "top_features",
        {}
    )

    X = pd.DataFrame(
        analysis_result.get("processed_X", [])
    )

    print("MAIN X TYPE:", type(X))
    print("MAIN X SHAPE:", X.shape)
    print(X.head())

    try:
        shap_file = generate_shap_explanation(
            model_object,
            X
        )
    except Exception as e:
        print("MAIN SHAP ERROR:")
        print(e)
        shap_file = str(e)

    analysis_result.pop("model_object", None)
    analysis_result.pop("processed_X", None)

    explanation = generate_explanation(
        feature_importance
    )

    store_memory(
        f"""
        target:{data_analysis['possible_target']}
        result:{analysis_result}
        """
    )

    past_memory = retrieve_memory(
        data_analysis["possible_target"]
    )

    critic_result = run_critic(
        df,
        data_analysis["possible_target"]
    )

    narrative_report = generate_narrative(
        data_analysis,
        analysis_result,
        critic_result,
        past_memory
    )

    print("DATA ANALYSIS:", data_analysis)

    profile = profile_data(df)

    print("PROFILE=", profile)

    insights = generate_insights(df)
    research_summary = generate_research_summary(insights)

    question_answer = answer_question(
        "Give a detailed analysis of this dataset",
        summary,
        insights,
        research_summary
    )

    chart_path = generate_chart(df)

    pdf_path = generate_pdf(
        summary,
        analysis_result,
        chart_path
    )

    for name, value in {
        "summary": summary,
        "profile": profile,
        "insights": insights,
        "research_summary": research_summary,
        "question_answer": question_answer,
        "data_analysis": data_analysis,
        "analysis_result": analysis_result,
        "explanation": explanation,
        "critic_result": critic_result,
        "narrative_report": narrative_report,
        "chart_path": chart_path,
        "pdf_path": pdf_path,
        "shap_file": shap_file
    }.items():
        print(name, type(value))

    print("SUMMARY")
    print(json.dumps(summary, default=str))

    print("PROFILE")
    print(json.dumps(profile, default=str))

    print("DATA_ANALYSIS")
    print(json.dumps(data_analysis, default=str))

    print("ANALYSIS_RESULT")
    print(json.dumps(analysis_result, default=str))

    print("EXPLANATION")
    print(json.dumps(explanation, default=str))

    print("CRITIC_RESULT")
    print(json.dumps(critic_result, default=str))

    print("TYPE CHECK")
    print(type(summary))
    print(type(profile))
    print(type(insights))
    print(type(data_analysis))
    print(type(analysis_result))
    print(type(critic_result))

    response = {
        "filename": file.filename,
        "summary": sanitize(summary),
        "profile": sanitize(profile),
        "insights": sanitize(insights),
        "research_summary": research_summary,
        "question_answer": question_answer,
        "data_analysis": sanitize(data_analysis),
        "analysis_result": sanitize(analysis_result),
        "explanation": sanitize(explanation),
        "critic_result": sanitize(critic_result),
        "narrative_report": narrative_report,
        "chart_file": chart_path,
        "pdf_file": pdf_path,
        "shap_file": shap_file
    }

    print(json.dumps(response, default=str))

    return jsonable_encoder(response)