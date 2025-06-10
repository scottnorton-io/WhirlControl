"""RecJam Feed module

Provides a simple data container for a read-only feed.
"""

from dataclasses import dataclass
from typing import List

@dataclass
class RecJamItem:
    title: str
    link: str


class RecJamFeed:
    def __init__(self) -> None:
        self.items: List[RecJamItem] = []

    def add_item(self, title: str, link: str) -> None:
        self.items.append(RecJamItem(title=title, link=link))

    def list_items(self) -> List[RecJamItem]:
        return self.items

    def remove_item(self, title: str) -> None:
        self.items = [item for item in self.items if item.title != title]

    def to_json(self) -> str:
        """Serialize feed items to JSON string."""
        import json

        return json.dumps(
            [{"title": item.title, "link": item.link} for item in self.items]
        )

    def to_markdown(self) -> str:
        """Return feed items formatted as a Markdown list."""
        lines = [f"- [{item.title}]({item.link})" for item in self.items]
        return "\n".join(lines)

    @classmethod
    def from_json(cls, data: str) -> "RecJamFeed":
        """Create a RecJamFeed from JSON string."""
        import json

        obj = cls()
        try:
            for entry in json.loads(data):
                obj.add_item(entry.get("title", ""), entry.get("link", ""))
        except Exception:
            pass
        return obj

    @classmethod
    def from_markdown(cls, data: str) -> "RecJamFeed":
        """Create a RecJamFeed from a Markdown bullet list."""
        obj = cls()
        for line in data.splitlines():
            line = line.strip()
            if line.startswith("- [") and "](" in line and line.endswith(")"):
                title_part, link_part = line[3:-1].split("](", 1)
                obj.add_item(title_part, link_part)
        return obj
