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
        self.members.append(Member(name=name, email=email, tags=tags))

    def find_member(self, email: str) -> Optional[Member]:
        for member in self.members:
            if member.email == email:
                return member
        return None
