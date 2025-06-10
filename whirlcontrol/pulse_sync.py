"""PulseSync module

Simulates weekly pulse survey interactions.
"""

from datetime import datetime
from typing import Dict, Iterable

from . import email_utils


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
            if delta_weeks >= PULSE_SKIP_THRESHOLD:
                statuses[member.email] = "low_engaged"
            else:
                statuses[member.email] = "active"
    return statuses


def send_pulse_emails(members: Iterable[str]) -> None:
    """Send a pulse survey email to each member."""
    email_utils.send_bulk_template(members, "weekly_pulse")


def weekly_pulse_cycle(whirl_list) -> Dict[str, str]:
    """Run the full weekly pulse process and return statuses."""
    emails = [member.email for member in whirl_list.members if "pulse_active" in member.tags]
    send_pulse_emails(emails)
    statuses = process_weekly_pulse(whirl_list)
    for email, status in statuses.items():
        if status == "low_engaged":
            whirl_list.add_tag(email, "low_engaged")
            email_utils.tag_mailchimp(email, "low_engaged")
        else:
            whirl_list.remove_tag(email, "low_engaged")
            email_utils.tag_mailchimp(email, "active")
    return statuses


def summary_metrics(whirl_list) -> Dict[str, int]:
    """Return counts of active and low engaged members."""
    statuses = process_weekly_pulse(whirl_list)
    counts = {"active": 0, "low_engaged": 0, "unknown": 0}
    for status in statuses.values():
        counts[status] += 1
    return counts
