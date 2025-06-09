"""Script to process weekly pulse engagements."""

from whirlcontrol import whirl_list, pulse_sync


def send_pulse_reminders():
    crm = whirl_list.WhirlList()
    crm.add_member("User One", "one@example.com", tags=["pulse_active"])
    pulse_sync.record_pulse_response(crm, "one@example.com")
    statuses = pulse_sync.weekly_pulse_cycle(crm)
    print(statuses)


if __name__ == "__main__":
    send_pulse_reminders()
