"""CourtSignal module

Provides a simplified representation of court status.
This MVP uses static data to simulate a court grid.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List

class CourtStatus(Enum):
    OPEN = "open"
    SOFT_RSVP = "soft_rsvp"
    CAPACITY = "capacity"

@dataclass
class Court:
    label: str
    status: CourtStatus


def get_court_grid() -> Dict[str, CourtStatus]:
    """Return current court status for courts A-D."""
    return {
        "A": CourtStatus.OPEN,
        "B": CourtStatus.CAPACITY,
        "C": CourtStatus.OPEN,
        "D": CourtStatus.SOFT_RSVP,
    }


def update_court_status(grid: Dict[str, CourtStatus], court: str, status: CourtStatus) -> None:
    """Update the status of a court label in the provided grid."""
    if court in grid:
        grid[court] = status


def grid_to_list(grid: Dict[str, CourtStatus]) -> List[Court]:
    """Convert a grid dict to a list of Court dataclasses."""
    return [Court(label=k, status=v) for k, v in grid.items()]


def list_to_grid(courts: List[Court]) -> Dict[str, CourtStatus]:
    """Convert a list of Court dataclasses back to a grid dict."""
    return {c.label: c.status for c in courts}
