"""Demo showing Airtable helper usage."""

from whirlcontrol import airtable_utils


def run():
    airtable_utils.update_airtable_record(
        "demo@example.com", {"Name": "Demo", "RSVP Status": "opted_in"}
    )
    record = airtable_utils.get_airtable_record("demo@example.com")
    print("Fetched record:", record)


if __name__ == "__main__":
    run()
