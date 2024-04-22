class Task:
    def __init__(self, task_id, title, description, priority, status):
        self.id = task_id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status

    def __str__(self):
        return f"ID: {self.id}, Title: {self.title}, Description: {self.description}, Priority: {self.priority}, Status: {self.status}"

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self):
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        priority = input("Enter task priority (High/Medium/Low): ").lower()
        status = input("Enter task status (Pending/In Progress/Completed): ").lower()

        if priority not in ["high", "medium", "low"]:
            print("Invalid priority. Please try again.")
            return

        if status not in ["pending", "in progress", "completed"]:
            print("Invalid status. Please try again.")
            return

        task_id = self.next_id
        task = Task(task_id, title, description, priority, status)
        self.tasks.append(task)
        self.next_id += 1
        print(f"Task added successfully with ID: {task_id}")

    def edit_task(self):
        task_id = int(input("Enter task ID to edit: "))
        task = self.get_task_by_id(task_id)

        if task:
            new_title = input("Enter new title (leave blank to keep current): ")
            new_description = input("Enter new description (leave blank to keep current): ")
            new_priority = input("Enter new priority (High/Medium/Low, leave blank to keep current): ").lower()
            new_status = input("Enter new status (Pending/In Progress/Completed, leave blank to keep current): ").lower()

            if new_title:
                task.title = new_title
            if new_description:
                task.description = new_description
            if new_priority and new_priority in ["high", "medium", "low"]:
                task.priority = new_priority
            if new_status and new_status in ["pending", "in progress", "completed"]:
                task.status = new_status

            print("Task updated successfully.")
        else:
            print(f"No task found with ID: {task_id}")

    def delete_task(self):
        task_id = int(input("Enter task ID to delete: "))
        task = self.get_task_by_id(task_id)

        if task:
            self.tasks.remove(task)
            print("Task deleted successfully.")
        else:
            print(f"No task found with ID: {task_id}")

    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def view_all_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("All Tasks:")
            for task in self.tasks:
                print(str(task))

    def filter_tasks_by_priority(self):
        priority = input("Enter priority to filter (High/Medium/Low): ").lower()

        if priority not in ["high", "medium", "low"]:
            print("Invalid priority. Please try again.")
            return

        filtered_tasks = [task for task in self.tasks if task.priority == priority]

        if not filtered_tasks:
            print(f"No tasks found with priority '{priority}'.")
        else:
            print(f"Tasks with priority '{priority}':")
            for task in filtered_tasks:
                print(str(task))

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. View All Tasks")
        print("5. Filter Tasks by Priority")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            task_manager.add_task()
        elif choice == "2":
            task_manager.edit_task()
        elif choice == "3":
            task_manager.delete_task()
        elif choice == "4":
            task_manager.view_all_tasks()
        elif choice == "5":
            task_manager.filter_tasks_by_priority()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()