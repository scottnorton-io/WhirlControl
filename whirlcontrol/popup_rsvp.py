"""PopUp RSVP module

Placeholder functions for RSVP handling.
"""

from typing import Dict


def handle_rsvp(payload: Dict[str, str], whirl_list) -> None:
    """Process an RSVP payload and update WhirlList."""
    email = payload.get("email")
    name = payload.get("name", "")
    zip_code = payload.get("zip")
    court = payload.get("court")
    if email:
        initial_tags = ["rsvp_optin"]
        tier = payload.get("tier")
        if tier:
            initial_tags.append(f"tier_{tier}")
        whirl_list.add_member(name, email, tags=initial_tags)
        if zip_code:
            whirl_list.add_tag(email, f"zip_{zip_code}")
        if court:
            whirl_list.add_tag(email, f"court_{court}")
