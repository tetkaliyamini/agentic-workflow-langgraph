# agents/tool_agent.py
class ToolAgent:
    def solve_task(self, task):
        """Solves each task based on predefined solutions."""
        solutions = {
            "Book a flight": "Flight booked successfully",
            "Find a hotel": "Hotel found and booked",
            "Plan sightseeing": "Sightseeing planned",
            "Research audience": "Audience research complete",
            "Find platforms": "Platforms found for marketing",
            "Create content": "Marketing content created"
        }
        return solutions.get(task, "Task not solved")

    def reflect_on_solution(self, task, solution):
        """Reflects on the task and provides feedback."""
        if solution == "Task not solved":
            return False
        return True
