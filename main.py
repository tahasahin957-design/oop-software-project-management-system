class User:
    def __init__(self, name, email, role):
        self.__name = name
        self.__email = email
        self.__role = role

    def get_name(self):
        return self.__name

    def get_role(self):
        return self.__role

    def display_info(self):
        print(f"Name: {self.__name}")
        print(f"Email: {self.__email}")
        print(f"Role: {self.__role}")


class Developer(User):
    def __init__(self, name, email, specialization):
        super().__init__(name, email, "Developer")
        self.__specialization = specialization
        self.__assigned_tasks = []

    def assign_task(self, task):
        self.__assigned_tasks.append(task)

    def view_tasks(self):
        if not self.__assigned_tasks:
            print(f"{self.get_name()} has no assigned tasks.")
        else:
            print(f"\nTasks assigned to {self.get_name()}:")
            for task in self.__assigned_tasks:
                print(f"- {task.title}")

    def display_info(self):
        print(f"Name: {self.get_name()}")
        print(f"Role: Developer")
        print(f"Specialization: {self.__specialization}")


class ProjectManager(User):
    def __init__(self, name, email):
        super().__init__(name, email, "Project Manager")

    def display_info(self):
        print(f"Name: {self.get_name()}")
        print("Role: Project Manager")


class Task:
    def __init__(self, title, description, priority, deadline):
        self.title = title
        self.__description = description
        self.__priority = priority
        self.__deadline = deadline
        self.__status = "Pending"
        self.__assigned_developer = None

    def assign_developer(self, developer):
        self.__assigned_developer = developer
        developer.assign_task(self)

    def update_status(self, new_status):
        self.__status = new_status

    def get_status(self):
        return self.__status

    def show_task_info(self):
        developer_name = (
            self.__assigned_developer.get_name()
            if self.__assigned_developer
            else "Not Assigned"
        )

        print("\n----------------------------")
        print(f"Task: {self.title}")
        print(f"Priority: {self.__priority}")
        print(f"Deadline: {self.__deadline}")
        print(f"Status: {self.__status}")
        print(f"Assigned Developer: {developer_name}")
        print("----------------------------")


class Project:
    def __init__(self, project_name):
        self.project_name = project_name
        self.developers = []
        self.tasks = []

    def add_developer(self, developer):
        self.developers.append(developer)

    def add_task(self, task):
        self.tasks.append(task)

    def show_progress(self):
        completed_tasks = sum(
            1 for task in self.tasks
            if task.get_status() == "Completed"
        )

        total_tasks = len(self.tasks)

        progress = (
            (completed_tasks / total_tasks) * 100
            if total_tasks > 0 else 0
        )

        print("\n===== Project Progress =====")
        print(f"Project Name: {self.project_name}")
        print(f"Completed Tasks: {completed_tasks}/{total_tasks}")
        print(f"Progress: {progress:.0f}%")
        print("============================")


class ProjectManagementSystem:
    def __init__(self):
        self.project = Project("E-Commerce Platform")
        self.load_demo_data()

    def load_demo_data(self):
        taha = Developer(
            "Taha Sahin",
            "taha@email.com",
            "Backend Developer"
        )

        kevin = Developer(
            "Kevin Miller",
            "kevin@email.com",
            "Frontend Developer"
        )

        emma = Developer(
            "Emma Wilson",
            "emma@email.com",
            "Database Engineer"
        )

        self.project.add_developer(taha)
        self.project.add_developer(kevin)
        self.project.add_developer(emma)

        task1 = Task(
            "User Authentication",
            "Implement login system",
            "High",
            "2026-06-15"
        )

        task2 = Task(
            "Homepage UI Design",
            "Design homepage interface",
            "Medium",
            "2026-06-20"
        )

        task3 = Task(
            "Database Integration",
            "Connect database to system",
            "High",
            "2026-06-22"
        )

        task4 = Task(
            "Payment System",
            "Develop payment feature",
            "Medium",
            "2026-06-25"
        )

        task1.assign_developer(taha)
        task2.assign_developer(kevin)
        task3.assign_developer(emma)
        task4.assign_developer(taha)

        task1.update_status("In Progress")
        task4.update_status("Completed")

        self.project.add_task(task1)
        self.project.add_task(task2)
        self.project.add_task(task3)
        self.project.add_task(task4)

    def view_developers(self):
        print("\n===== Developers =====")
        for developer in self.project.developers:
            developer.display_info()
            print()

    def view_tasks(self):
        print("\n===== Task List =====")
        for task in self.project.tasks:
            task.show_task_info()

    def update_task_status(self):
        print("\nSelect a task to update:")

        for index, task in enumerate(self.project.tasks, start=1):
            print(f"{index}. {task.title}")

        try:
            choice = int(input("Enter task number: ")) - 1

            if 0 <= choice < len(self.project.tasks):
                new_status = input(
                    "Enter new status "
                    "(Pending/In Progress/Completed): "
                )

                self.project.tasks[choice].update_status(
                    new_status
                )

                print("Task status updated successfully!")

            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")

    def run(self):
        while True:
            print("\n===== Software Project Management System =====")
            print("1. View Developers")
            print("2. View Tasks")
            print("3. Update Task Status")
            print("4. Show Project Progress")
            print("5. Exit")

            choice = input("Select an option: ")

            if choice == "1":
                self.view_developers()

            elif choice == "2":
                self.view_tasks()

            elif choice == "3":
                self.update_task_status()

            elif choice == "4":
                self.project.show_progress()

            elif choice == "5":
                print("Exiting system...")
                break

            else:
                print("Invalid option. Please try again.")


system = ProjectManagementSystem()
system.run()
