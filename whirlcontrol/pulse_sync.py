"""PulseSync module

Simulates weekly pulse survey interactions.
"""

from datetime import datetime
from typing import Dict


def record_pulse_response(whirl_list, email: str) -> None:
    """Update the WhirlList with last pulse timestamp."""
    member = whirl_list.find_member(email)
    if member:
        setattr(member, "pulse_last_seen", datetime.utcnow())


# Example of automation pseudocode in code form
PULSE_SKIP_THRESHOLD = 3

def process_weekly_pulse(whirl_list) -> Dict[str, str]:
    """Return engagement status based on last pulse response."""
    statuses = {}
    for member in whirl_list.members:
        last_seen = getattr(member, "pulse_last_seen", None)
        if last_seen is None:
            statuses[member.email] = "unknown"
        else:
            delta_weeks = (datetime.utcnow() - last_seen).days // 7
            statuses[member.email] = "low_engaged" if delta_weeks >= PULSE_SKIP_THRESHOLD else "active"
    return statuses
