import os
import matplotlib.pyplot as plt

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_chart(df):

    os.makedirs("reports", exist_ok=True)

    numeric_cols = list(
        df.select_dtypes(include=["number"]).columns
    )

    ignore_cols = [
        "Phone_No.",
        "Phone No.",
        "Phone_No"
    ]

    numeric_cols = [
        c for c in numeric_cols
        if c not in ignore_cols
    ]

    if len(numeric_cols) == 0:
        return None

    col = numeric_cols[0]

    print("Selected chart column:", col)

    plt.figure(figsize=(8, 5))

    df[col].hist()

    plt.title(f"Distribution of {col}")

    chart_path = "reports/chart.png"

    plt.savefig(chart_path)

    plt.close()

    return chart_path


def generate_pdf(summary, analysis, chart_path):

    os.makedirs("reports", exist_ok=True)

    pdf_path = "reports/analysis_report.pdf"

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "ARIA Analysis Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 12))
    summary_text = f"""
    Rows: {summary['rows']}
    Columns: {summary['columns']}
    """

    analysis_text = f"""
    Problem Type: {analysis['problem_type']}
    Best Model: {analysis['best_model']}
    Score: {analysis['score']}
    """
    
    content.append(
        Paragraph(
    summary_text,
    styles["BodyText"]
)
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
    analysis_text,
    styles["BodyText"]
)
    )

    content.append(Spacer(1, 12))

    if chart_path:
        content.append(
            Image(
                chart_path,
                width=400,
                height=250
            )
        )

    doc.build(content)

    return pdf_path