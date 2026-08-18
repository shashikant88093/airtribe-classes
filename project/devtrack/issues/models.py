from abc import ABC, abstractmethod
from datetime import datetime


class BaseEntity(ABC):
    @abstractmethod
    def validate(self):
        pass

    def to_dict(self):
        return {key: value for key, value in self.__dict__.items()}


class Reporter(BaseEntity):
    def __init__(self, id, name, email, team):
        self.id = id
        self.name = name
        self.email = email
        self.team = team

    def validate(self):
        if not self.name or not str(self.name).strip():
            raise ValueError("Name cannot be empty")
        if not self.email or "@" not in str(self.email):
            raise ValueError("Invalid email")


class Issue(BaseEntity):
    ALLOWED_STATUS = {"open", "in_progress", "resolved", "closed"}
    ALLOWED_PRIORITY = {"low", "medium", "high", "critical"}

    def __init__(self, id, title, description, status, priority, reporter_id, created_at=None):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.reporter_id = reporter_id
        self.created_at = created_at or str(datetime.now())

    def validate(self):
        if not self.title or not str(self.title).strip():
            raise ValueError("Title cannot be empty")
        if self.status not in self.ALLOWED_STATUS:
            raise ValueError(f"Invalid status. Must be one of: {', '.join(sorted(self.ALLOWED_STATUS))}")
        if self.priority not in self.ALLOWED_PRIORITY:
            raise ValueError(f"Invalid priority. Must be one of: {', '.join(sorted(self.ALLOWED_PRIORITY))}")

    def describe(self):
        return f"{self.title} [{self.priority}]"


class CriticalIssue(Issue):
    def describe(self):
        return f"[URGENT] {self.title} — needs immediate attention"


class LowPriorityIssue(Issue):
    def describe(self):
        return f"{self.title} — low priority, handle when free"