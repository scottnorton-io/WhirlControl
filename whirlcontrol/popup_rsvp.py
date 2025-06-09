"""PopUp RSVP module

Placeholder functions for RSVP handling.
"""

from typing import Dict


def handle_rsvp(payload: Dict[str, str], whirl_list) -> None:
    """Process an RSVP payload and update WhirlList."""
    email = payload.get("email")
    name = payload.get("name", "")
    if email:
        whirl_list.add_member(name, email, tags=["rsvp_optin"])
