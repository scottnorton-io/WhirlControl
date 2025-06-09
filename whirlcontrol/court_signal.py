"""CourtSignal module

Provides a simplified representation of court status.
This MVP uses static data to simulate a court grid.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Dict

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
    # Placeholder logic; in real system this might query Webflow or Airtable
    return {
        "A": CourtStatus.OPEN,
        "B": CourtStatus.CAPACITY,
        "C": CourtStatus.OPEN,
        "D": CourtStatus.SOFT_RSVP,
    }
