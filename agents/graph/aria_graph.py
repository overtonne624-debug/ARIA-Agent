from langgraph.graph import StateGraph, END

from agents.data_agent import analyze_dataset
from agents.analysis_agent import run_analysis
from agents.explainability_agent import generate_shap_explanation
from agents.critic_agent import run_critic
from agents.narrative_agent import generate_narrative
from agents.memory_agent import store_memory, retrieve_memory


from typing import TypedDict
import pandas as pd

class ARIAState(TypedDict):
    df: pd.DataFrame
    data_result: dict
    analysis_result: dict
    explainability_result: dict
    critic_result: dict
    narrative: str
    memory_result: dict


def data_node(state):
    print("Running Data Agent...")
    print("STATE KEYS:", list(state.keys()))
    print("STATE:", state)

    df = state.get("df")

    if df is None:
        raise ValueError("df not found in state")

    data_result = analyze_dataset(df)
    state["data_result"] = data_result
    return state


def analysis_node(state):
    print("Running Analysis Agent...")

    df = state["df"]
    target = state["data_result"]["possible_target"]
    analysis_result = run_analysis(df, target)
    state["analysis_result"] = analysis_result
    return state


def explainability_node(state):
    print("Running Explainability Agent...")

    model = state["analysis_result"]["model_object"]
    X = state["analysis_result"]["processed_X"]
    shap_result = generate_shap_explanation(model, X)
    state["shap_result"] = shap_result
    return state


def critic_node(state):
    print("Running Critic Agent...")

    df = state["df"]
    target = state["data_result"]["possible_target"]
    critic_result = run_critic(df, target)
    state["critic_result"] = critic_result
    return state


def narrative_node(state):
    print("Running Narrative Agent...")

    memory = retrieve_memory("latest")

    narrative = generate_narrative(
        state["data_result"],
        state["analysis_result"],
        state["critic_result"],
        memory
    )

    print("NARRATIVE =", narrative)

    state["narrative"] = narrative

    print("STATE KEYS AFTER NARRATIVE:")
    print(list(state.keys()))

    return state


def memory_node(state):
    print("Running Memory Agent...")

    print("MEMORY NODE KEYS:")
    print(list(state.keys()))

    print("FULL STATE:")
    print(state)

    if "narrative" not in state:
        print("ERROR: narrative missing")
        return state

    if "narrative" in state:
      store_memory(state["narrative"])

    return state


builder = StateGraph(ARIAState)

builder.add_node("data", data_node)
builder.add_node("analysis", analysis_node)
builder.add_node("explainability", explainability_node)
builder.add_node("critic", critic_node)
builder.add_node("narrative", narrative_node)
builder.add_node("memory", memory_node)

builder.set_entry_point("data")

builder.add_edge("data", "analysis")
builder.add_edge("analysis", "explainability")
builder.add_edge("explainability", "critic")
builder.add_edge("critic", "narrative")
builder.add_edge("narrative", "memory")
builder.add_edge("memory", END)

graph = builder.compile()

if __name__ == "__main__":
    import pandas as pd

    df = pd.read_csv("datasets/student_dataset_v1.csv")

initial_state = {
    "df": df
}

graph.invoke(initial_state)