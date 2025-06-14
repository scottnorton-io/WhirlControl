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


def grid_to_json(grid: Dict[str, CourtStatus]) -> str:
    """Serialize the court grid to a JSON string."""
    import json

    return json.dumps({label: status.value for label, status in grid.items()})


def grid_from_json(data: str) -> Dict[str, CourtStatus]:
    """Recreate a court grid from a JSON string."""
    import json

    obj = json.loads(data)
    grid: Dict[str, CourtStatus] = {}
    for label, status_val in obj.items():
        try:
            grid[label] = CourtStatus(status_val)
        except ValueError:
            grid[label] = CourtStatus.OPEN
    return grid


def next_status(status: CourtStatus) -> CourtStatus:
    """Cycle to the next status in order OPEN -> SOFT_RSVP -> CAPACITY -> OPEN."""
    order = [CourtStatus.OPEN, CourtStatus.SOFT_RSVP, CourtStatus.CAPACITY]
    try:
        idx = order.index(status)
        return order[(idx + 1) % len(order)]
    except ValueError:
        return CourtStatus.OPEN


def toggle_court_status(grid: Dict[str, CourtStatus], court: str) -> None:
    """Advance the status of a court in the grid using ``next_status``."""
    if court in grid:
        grid[court] = next_status(grid[court])
