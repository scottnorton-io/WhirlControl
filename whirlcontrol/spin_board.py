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
