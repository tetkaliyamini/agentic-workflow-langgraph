# agents/feedback_agent.py
class FeedbackAgent:
    def refine(self, task, solution):
        """Refines the task if the solution is not satisfactory."""
        if solution == "Task not solved":
            return f"Refining task: {task}"
        return f"Task '{task}' completed successfully"
