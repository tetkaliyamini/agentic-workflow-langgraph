 Agentic Workflow using Langgraph

This project implements an Agentic Workflow that leverages Langgraph to decompose a user's query into smaller tasks, solve them using a tool-based approach, and refine the solutions using a feedback loop. This setup includes three agents:

PlanAgent: Splits the query into subtasks.
ToolAgent: Solves each subtask.
FeedbackAgent: Refines and reviews the results for accuracy.
The goal is to demonstrate how AI agents can automate task planning, execution, and feedback in a modular workflow.
