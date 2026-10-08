"""Task manager application with projects, tasks, and reporting."""

from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from typing import Optional


class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    URGENT = 4


class Status(Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"
    CANCELLED = "cancelled"


@dataclass
class Task:
    title: str
    description: str
    priority: Priority
    status: Status = Status.TODO
    assignee: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)
    due_date: Optional[datetime] = None
    tags: list[str] = field(default_factory=list)

    def is_overdue(self) -> bool:
        if self.due_date is None:
            return False
        return datetime.now() > self.due_date and self.status != Status.DONE

    def days_until_due(self) -> Optional[int]:
        if self.due_date is None:
            return None
        delta = self.due_date - datetime.now()
        return delta.days

    def mark_done(self) -> None:
        self.status = Status.DONE

    def mark_in_progress(self) -> None:
        self.status = Status.IN_PROGRESS

    def add_tag(self, tag: str) -> None:
        if tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag: str) -> None:
        self.tags = [t for t in self.tags if t != tag]

    def summary(self) -> str:
        flag = " [OVERDUE]" if self.is_overdue() else ""
        return f"[{self.priority.name}] {self.title}{flag}"


@dataclass
class Project:
    name: str
    description: str
    tasks: list[Task] = field(default_factory=list)
    owner: str = "unassigned"

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def remove_task(self, title: str) -> None:
        self.tasks = [t for t in self.tasks if t.title != title]

    def get_tasks_by_status(self, status: Status) -> list[Task]:
        return [t for t in self.tasks if t.status == status]

    def get_tasks_by_priority(self, priority: Priority) -> list[Task]:
        return [t for t in self.tasks if t.priority == priority]

    def get_overdue_tasks(self) -> list[Task]:
        return [t for t in self.tasks if t.is_overdue()]

    def completion_rate(self) -> float:
        if not self.tasks:
            return 0.0
        done = len(self.get_tasks_by_status(Status.DONE))
        return done / len(self.tasks) * 100

    def task_count(self) -> dict[str, int]:
        counts = {}
        for status in Status:
            tasks = self.get_tasks_by_status(status)
            counts[status.value] = len(tasks)
        return counts


class TaskManager:
    def __init__(self):
        self.projects: list[Project] = []

    def create_project(self, name: str, description: str, owner: str) -> Project:
        project = Project(name=name, description=description, owner=owner)
        self.projects.append(project)
        return project

    def find_project(self, name: str) -> Optional[Project]:
        for project in self.projects:
            if project.name == name:
                return project
        return None

    def delete_project(self, name: str) -> bool:
        before = len(self.projects)
        self.projects = [p for p in self.projects if p.name != name]
        return len(self.projects) < before

    def all_tasks(self) -> list[Task]:
        result = []
        for project in self.projects:
            result.extend(project.tasks)
        return result

    def overdue_report(self) -> str:
        lines = ["=== Overdue Tasks ==="]
        for project in self.projects:
            overdue = project.get_overdue_tasks()
            if overdue:
                lines.append(f"\nProject: {project.name}")
                for task in overdue:
                    lines.append(f"  - {task.summary()}")
        return "\n".join(lines)

    def dashboard(self) -> str:
        lines = ["=== Task Dashboard ==="]
        total_tasks = 0
        total_done = 0
        for project in self.projects:
            counts = project.task_count()
            total = sum(counts.values())
            done = counts.get("done", 0)
            total_tasks += total
            total_done += done
            pct = project.completion_rate()
            lines.append(f"\n{project.name} ({pct:.0f}% complete)")
            lines.append(f"  TODO: {counts.get('todo', 0)}")
            lines.append(f"  In Progress: {counts.get('in_progress', 0)}")
            lines.append(f"  Done: {counts.get('done', 0)}")
            lines.append(f"  Cancelled: {counts.get('cancelled', 0)}")

        if total_tasks > 0:
            overall = total_done / total_tasks * 100
            lines.append(f"\nOverall: {overall:.0f}% complete ({total_done}/{total_tasks})")
        return "\n".join(lines)


def create_sample_data() -> TaskManager:
    manager = TaskManager()

    web = manager.create_project("Website Redesign", "Modernize the company website", "Alice")
    web.add_task(Task("Update homepage", "Redesign the landing page", Priority.HIGH))
    web.add_task(Task("Fix navbar", "Navigation broken on mobile", Priority.URGENT))
    web.add_task(Task("Add dark mode", "Implement dark theme toggle", Priority.MEDIUM))
    web.add_task(Task("Write tests", "Add unit tests for components", Priority.LOW))
    web.add_task(Task("SEO audit", "Run lighthouse and fix issues", Priority.MEDIUM))

    api = manager.create_project("API Migration", "Move from REST to GraphQL", "Bob")
    api.add_task(Task("Schema design", "Design the GraphQL schema", Priority.HIGH))
    api.add_task(Task("Auth middleware", "Port authentication layer", Priority.URGENT))
    api.add_task(Task("Rate limiting", "Implement rate limiter", Priority.MEDIUM))
    api.add_task(Task("Documentation", "Write API docs with examples", Priority.LOW))

    mobile = manager.create_project("Mobile App", "Cross-platform mobile application", "Charlie")
    mobile.add_task(Task("Login screen", "Build login and signup flow", Priority.HIGH))
    mobile.add_task(Task("Push notifications", "Set up FCM integration", Priority.MEDIUM))
    mobile.add_task(Task("Offline mode", "Cache data for offline use", Priority.LOW))
    mobile.add_task(Task("App store listing", "Prepare screenshots and description", Priority.LOW))

    return manager


def main():
    manager = create_sample_data()

    web = manager.find_project("Website Redesign")
    if web:
        web.tasks[0].mark_done()
        web.tasks[1].mark_in_progress()
        web.tasks[0].add_tag("frontend")
        web.tasks[1].add_tag("bug")
        web.tasks[1].add_tag("mobile")

    api = manager.find_project("API Migration")
    if api:
        api.tasks[0].mark_done()
        api.tasks[0].add_tag("backend")
        api.tasks[1].mark_in_progress()

    print(manager.dashboard())
    print()
    print(manager.overdue_report())


if __name__ == "__main__":
    main()
