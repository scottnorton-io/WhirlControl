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

    # New helper methods for basic CRM manipulation

    def remove_tag(self, email: str, tag: str) -> None:
        """Remove a tag from a member if present."""
        member = self.find_member(email)
        if member and tag in member.tags:
            member.tags.remove(tag)

    def list_by_tag(self, tag: str) -> List[Member]:
        """Return members who have the specified tag."""
        return [m for m in self.members if tag in m.tags]

    def to_json(self) -> str:
        """Serialize members to JSON string."""
        import json

        def member_to_dict(m: Member) -> dict:
            return {"name": m.name, "email": m.email, "tags": list(m.tags)}

        return json.dumps([member_to_dict(m) for m in self.members])

    @classmethod
    def from_json(cls, data: str) -> "WhirlList":
        """Create a WhirlList instance from JSON string."""
        import json

        obj = cls()
        try:
            for entry in json.loads(data):
                obj.add_member(entry.get("name", ""), entry.get("email", ""), entry.get("tags", []))
        except Exception:
            pass
        return obj
