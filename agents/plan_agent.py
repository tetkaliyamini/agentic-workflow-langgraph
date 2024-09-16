# agents/plan_agent.py
class PlanAgent:
    def split_query(self, query):
        """Splits a user's query into smaller, manageable tasks."""
        if "trip" in query:
            return ["Book a flight", "Find a hotel", "Plan sightseeing"]
        elif "marketing" in query:
            return ["Research audience", "Find platforms", "Create content"]
        else:
            return ["Unknown task"]

    def modify_task(self, task):
        """Simulates a modification of a task."""
        return f"Modified {task}"

    def delete_task(self, task):
        """Simulates deletion of a task."""
        return f"Deleted {task}"

    def add_task(self, task):
        """Simulates addition of a new task."""
        return f"Added {task}"
