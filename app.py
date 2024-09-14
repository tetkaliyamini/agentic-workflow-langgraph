import streamlit as st
from agents.plan_agent import PlanAgent
from agents.tool_agent import ToolAgent
from agents.feedback_agent import FeedbackAgent

def main():
    # Initialize agents
    plan_agent = PlanAgent()
    tool_agent = ToolAgent()
    feedback_agent = FeedbackAgent()

    # Streamlit app header
    st.title("Langgraph Agentic Workflow")
    st.write("Enter your query to get started:")

    # User input
    user_query = st.text_input("User Query")

    if user_query:
        # PlanAgent splits the query into smaller tasks
        tasks = plan_agent.split_query(user_query)
        st.write(f"Tasks created by PlanAgent: {tasks}")

        # ToolAgent solves each task
        results = {}
        for task in tasks:
            result = tool_agent.solve_task(task)
            feedback = feedback_agent.refine(task, result)
            results[task] = feedback
            st.write(f"Result for {task}: {result} -> Feedback: {feedback}")

        # Final Output
        st.subheader("Final Results")
        st.write(results)

if __name__ == "__main__":
    main()
