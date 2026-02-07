class SimpleAgent:
    def __init__(self, goal):
        self.goal = goal
        self.tasks = []
        self.completed_tasks = []

    def plan_tasks(self):
        print("Planning tasks...")
        self.tasks = [
            "Understand the goal",
            "Gather information",
            "Process information",
            "Generate output"
        ]

    def decide_next_action(self):
        if self.tasks:
            return self.tasks.pop(0)
        return None

    def execute_action(self, action):
        print(f"Executing: {action}")
        self.completed_tasks.append(action)

    def review_progress(self):
        print("Reviewing progress...")
        return len(self.tasks) == 0

    def run(self):
        print(f"Agent started with goal: {self.goal}")
        self.plan_tasks()

        while True:
            action = self.decide_next_action()
            if not action:
                break

            self.execute_action(action)

            if self.review_progress():
                break

        print("Goal achieved!")
        print("Completed tasks:", self.completed_tasks)


if __name__ == "__main__":
    agent = SimpleAgent("Create a summary for a given topic")
    agent.run()
