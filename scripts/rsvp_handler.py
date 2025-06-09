"""Example webhook handler for RSVP submissions."""

from whirlcontrol import popup_rsvp, whirl_list


def handle_rsvp_webhook(payload):
    crm = whirl_list.WhirlList()
    popup_rsvp.handle_rsvp(payload, crm)
    # In real use, you would persist the crm data or sync to Airtable
    for member in crm.list_members():
        print(member)


if __name__ == "__main__":
    sample_payload = {
        "email": "user@example.com",
        "name": "Sample User",
        "zip": "85001",
        "court": "A",
    }
    handle_rsvp_webhook(sample_payload)
