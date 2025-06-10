"""Demo using WhirlList CSV helpers."""
from whirlcontrol import whirl_list


def csv_demo():
    crm = whirl_list.WhirlList()
    crm.add_member("Alice", "alice@example.com", tags=["founding_member"])
    crm.add_member("Bob", "bob@example.com", tags=["rsvp_optin", "pulse_active"])
    csv_data = crm.to_csv()
    print("CSV Export:\n", csv_data)

    new_crm = whirl_list.WhirlList.from_csv(csv_data)
    for member in new_crm.list_members():
        print(f"Loaded {member.email} with tags {member.tags}")


if __name__ == "__main__":
    csv_demo()
