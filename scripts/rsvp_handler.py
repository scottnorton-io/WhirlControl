"""Example webhook handler for RSVP submissions."""

from whirlcontrol import popup_rsvp, whirl_list


def handle_rsvp_webhook(payload):
    crm = whirl_list.WhirlList()
    popup_rsvp.handle_rsvp(payload, crm)
    # In real use, you would persist the crm data or sync to Airtable
    print(crm.members)


if __name__ == "__main__":
    sample_payload = {"email": "user@example.com", "name": "Sample User"}
    handle_rsvp_webhook(sample_payload)
