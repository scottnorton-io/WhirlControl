"""Script to process weekly pulse engagements."""

from whirlcontrol import whirl_list, pulse_sync


def send_pulse_reminders():
    crm = whirl_list.WhirlList()
    crm.add_member("User One", "one@example.com")
    pulse_sync.record_pulse_response(crm, "one@example.com")
    statuses = pulse_sync.process_weekly_pulse(crm)
    print(statuses)


if __name__ == "__main__":
    send_pulse_reminders()
