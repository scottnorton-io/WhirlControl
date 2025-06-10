"""Script to process weekly pulse engagements."""

from whirlcontrol import whirl_list, pulse_sync


def send_pulse_reminders():
    crm = whirl_list.WhirlList()
    crm.add_member("User One", "one@example.com", tags=["pulse_active"])
    crm.add_member("User Two", "two@example.com", tags=["pulse_active"])
    # Record a pulse for User One only
    pulse_sync.record_pulse_response(crm, "one@example.com")
    statuses = pulse_sync.weekly_pulse_cycle(crm)
    for member in crm.list_members():
        last_seen = getattr(member, "pulse_last_seen", None)
        print(member.email, member.tags, last_seen is not None)
    print("Statuses:", statuses)


if __name__ == "__main__":
    send_pulse_reminders()
