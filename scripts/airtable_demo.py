"""Demo showing Airtable helper usage."""

from whirlcontrol import airtable_utils


def run():
    airtable_utils.update_airtable_record(
        "demo@example.com", {"Name": "Demo", "RSVP Status": "opted_in"}
    )
    record = airtable_utils.get_airtable_record("demo@example.com")
    print("Fetched record:", record)

    airtable_utils.update_airtable_record(
        "second@example.com", {"Name": "Second", "RSVP Status": "opted_in"}
    )
    print("All records:")
    for r in airtable_utils.list_airtable_records():
        print(r)

    # demonstrate deleting a record
    airtable_utils.delete_airtable_record("demo@example.com")
    print("After delete:")
    for r in airtable_utils.list_airtable_records():
        print(r)


if __name__ == "__main__":
    run()
