"""PopUp RSVP module

Placeholder functions for RSVP handling.
"""

from typing import Dict

from . import email_utils, airtable_utils


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
        airtable_utils.update_airtable_record(email, {
            "Name": name,
            "RSVP Status": "opted_in",
            "Tags": ",".join(initial_tags),
        })
        for tag in initial_tags:
            email_utils.tag_mailchimp(email, tag)
        if zip_code:
            tag = f"zip_{zip_code}"
            whirl_list.add_tag(email, tag)
            email_utils.tag_mailchimp(email, tag)
            airtable_utils.update_airtable_record(email, {"Zip Code": zip_code})
        if court:
            tag = f"court_{court}"
            whirl_list.add_tag(email, tag)
            email_utils.tag_mailchimp(email, tag)
            airtable_utils.update_airtable_record(email, {"Court": court})
