"""SpinBoard module

Holds community shoutouts and highlights for display.
"""

from dataclasses import dataclass
from typing import List, Optional

@dataclass
class WhirlMoment:
    title: str
    description: str


class SpinBoard:
    def __init__(self) -> None:
        self.moments: List[WhirlMoment] = []

    def add_moment(self, title: str, description: str) -> None:
        self.moments.append(WhirlMoment(title=title, description=description))

    def list_moments(self) -> List[WhirlMoment]:
        return self.moments

    def find_moment(self, title: str) -> Optional[WhirlMoment]:
        for moment in self.moments:
            if moment.title == title:
                return moment
        return None

    def remove_moment(self, title: str) -> None:
        self.moments = [m for m in self.moments if m.title != title]

    def to_markdown(self) -> str:
        """Return the moments formatted as a Markdown list."""
        lines = [f"- **{m.title}**: {m.description}" for m in self.moments]
        return "\n".join(lines)

    def to_json(self) -> str:
        """Serialize moments to a JSON string."""
        import json

        return json.dumps(
            [{"title": m.title, "description": m.description} for m in self.moments]
        )

    @classmethod
    def from_markdown(cls, data: str) -> "SpinBoard":
        """Create a SpinBoard from a Markdown bullet list."""
        obj = cls()
        for line in data.splitlines():
            line = line.strip()
            if not line.startswith("- "):
                continue
            content = line[2:]
            if content.startswith("**") and "**:" in content:
                title_part, desc = content[2:].split("**:", 1)
                title = title_part.strip()
                obj.add_moment(title, desc.strip())
        return obj

    @classmethod
    def from_json(cls, data: str) -> "SpinBoard":
        """Create a SpinBoard from a JSON list structure."""
        import json

        obj = cls()
        try:
            for entry in json.loads(data):
                obj.add_moment(entry.get("title", ""), entry.get("description", ""))
        except Exception:
            pass
        return obj
