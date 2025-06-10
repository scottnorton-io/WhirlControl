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
