def generate_research_summary(insights):
    return (
        "This dataset contains student academic information. "
        + " Key findings: "
        + ", ".join(insights[:5])
    )