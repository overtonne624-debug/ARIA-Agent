from langgraph.graph import StateGraph, END

class ARIAState(dict):
    pass

def data_node(state):
    print("Running Data Agent...")
    return state

def analysis_node(state):
    print("Running Analysis Agent...")
    return state

def explainability_node(state):
    print("Running Explainability Agent...")
    return state

def critic_node(state):
    print("Running Critic Agent...")
    return state

def narrative_node(state):
    print("Running Narrative Agent...")
    return state

def memory_node(state):
    print("Running Memory Agent...")
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
    graph.invoke({})