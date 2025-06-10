"""Demo script for WhirlList JSON export/import."""
from whirlcontrol import whirl_list


def export_import_demo():
    crm = whirl_list.WhirlList()
    crm.add_member("Alice", "alice@example.com", tags=["founding_member"])
    crm.add_member("Bob", "bob@example.com", tags=["rsvp_optin"])
    json_str = crm.to_json()
    print("Exported JSON:", json_str)

    # rebuild from JSON
    new_crm = whirl_list.WhirlList.from_json(json_str)
    for member in new_crm.list_members():
        print(f"Loaded {member.name} with tags {member.tags}")


if __name__ == "__main__":
    export_import_demo()
