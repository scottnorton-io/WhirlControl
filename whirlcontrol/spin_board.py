"""SpinBoard module

Holds community shoutouts and highlights for display.
"""

from dataclasses import dataclass
from typing import List

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
