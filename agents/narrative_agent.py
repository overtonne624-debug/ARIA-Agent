def generate_narrative(
    data_analysis,
    analysis_result,
    critic_result,
    past_memory
):

    target = data_analysis["possible_target"]

    model = analysis_result.get(
        "best_model",
        "Unknown"
    )

    score = analysis_result.get(
        "score",
        0
    )

    confidence = critic_result.get(
        "confidence",
        0
    )

    warnings = critic_result.get(
        "warnings",
        []
    )

    report = f"""
EXECUTIVE SUMMARY

ARIA analyzed the uploaded dataset.

Target Variable:
{target}

Best Model:
{model}

Model Score:
{score}

Confidence Score:
{confidence}

Warnings:
{', '.join(warnings) if warnings else 'None'}
memory context:
{past_memory}

RECOMMENDATIONS

1. Investigate top important features.
2. Improve data quality.
3. Reduce missing values.
4. Collect additional samples if possible.
5. Monitor model performance regularly.

CONCLUSION

The dataset was successfully analyzed by ARIA's multi-agent system.
"""

    return report