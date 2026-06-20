from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from agents import (
    build_search_agent,
    build_reader_agent,
    writer_chain,
    critic_chain
)


# ---------- STATE ----------

class ResearchState(TypedDict):
    topic: str
    search_results: str
    scraped_content: str
    report: str
    feedback: str


# ---------- NODE 1 : SEARCH ----------

def search_node(state: ResearchState):

    print("\n" + "="*50)
    print("Step 1 - Search Agent")
    print("="*50)

    search_agent = build_search_agent()

    result = search_agent.invoke({
        "messages": [
            (
                "user",
                f"Find recent, reliable and detailed information about {state['topic']}"
            )
        ]
    })

    return {
        "search_results": result["messages"][-1].content
    }


# ---------- NODE 2 : READER ----------

def reader_node(state: ResearchState):

    print("\n" + "="*50)
    print("Step 2 - Reader Agent")
    print("="*50)

    reader_agent = build_reader_agent()

    result = reader_agent.invoke({
        "messages": [
            (
                "user",
                f"""Based on the following search results about '{state['topic']}',
pick the most relevant URL and scrape it for deeper content.

Search Results:

{state['search_results'][:800]}
"""
            )
        ]
    })

    return {
        "scraped_content": result["messages"][-1].content
    }


# ---------- NODE 3 : WRITER ----------

def writer_node(state: ResearchState):

    print("\n" + "="*50)
    print("Step 3 - Writer")
    print("="*50)

    research_combined = (

        f"SEARCH RESULTS:\n"

        f"{state['search_results']}\n\n"

        f"DETAILED SCRAPED CONTENT:\n"

        f"{state['scraped_content']}"

    )

    report = writer_chain.invoke({

        "topic": state["topic"],

        "research": research_combined

    })

    return {

        "report": report

    }


# ---------- NODE 4 : CRITIC ----------

def critic_node(state: ResearchState):

    print("\n" + "="*50)
    print("Step 4 - Critic")
    print("="*50)

    feedback = critic_chain.invoke({

        "report": state["report"]

    })

    return {

        "feedback": feedback

    }


# ---------- BUILD GRAPH ----------

graph = StateGraph(ResearchState)

graph.add_node("search", search_node)

graph.add_node("reader", reader_node)

graph.add_node("writer", writer_node)

graph.add_node("critic", critic_node)


graph.add_edge(START, "search")

graph.add_edge("search", "reader")

graph.add_edge("reader", "writer")

graph.add_edge("writer", "critic")

graph.add_edge("critic", END)


app = graph.compile()


# ---------- RUN ----------

if __name__ == "__main__":

    topic = input("\nEnter a research topic: ")

    result = app.invoke({

        "topic": topic

    })

    print("\n")

    print("="*50)

    print("FINAL REPORT")

    print("="*50)

    print(result["report"])


    print("\n")

    print("="*50)

    print("CRITIC FEEDBACK")

    print("="*50)

    print(result["feedback"])