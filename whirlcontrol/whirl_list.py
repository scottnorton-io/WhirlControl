"""WhirlList module

Represents a minimal CRM model and tag handling.
This example uses an in-memory list to track members.
"""

from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Member:
    name: str
    email: str
    tags: List[str] = field(default_factory=list)


class WhirlList:
    def __init__(self) -> None:
        self.members: List[Member] = []

    def add_member(self, name: str, email: str, tags: Optional[List[str]] = None) -> None:
        tags = tags or []
        # Prevent duplicates based on email
        existing = self.find_member(email)
        if existing is None:
            self.members.append(Member(name=name, email=email, tags=tags))
        else:
            existing.name = name or existing.name
            for tag in tags:
                if tag not in existing.tags:
                    existing.tags.append(tag)

    def find_member(self, email: str) -> Optional[Member]:
        for member in self.members:
            if member.email == email:
                return member
        return None

    def list_members(self) -> List[Member]:
        return list(self.members)

    def add_tag(self, email: str, tag: str) -> None:
        member = self.find_member(email)
        if member and tag not in member.tags:
            member.tags.append(tag)

    def remove_member(self, email: str) -> None:
        self.members = [m for m in self.members if m.email != email]
