from whirlcontrol import whirl_list, pulse_sync


def gather_metrics(crm: whirl_list.WhirlList) -> dict:
    """Return simple metrics about member engagement."""
    statuses = pulse_sync.process_weekly_pulse(crm)
    counts = {"active": 0, "low_engaged": 0, "unknown": 0}
    for status in statuses.values():
        counts[status] += 1
    return counts


def demo_report():
    crm = whirl_list.WhirlList()
    crm.add_member("Alice", "alice@example.com", tags=["pulse_active"])
    crm.add_member("Bob", "bob@example.com", tags=["pulse_active"])
    pulse_sync.record_pulse_response(crm, "alice@example.com")
    metrics = gather_metrics(crm)
    print("Pulse metrics:", metrics)


if __name__ == "__main__":
    demo_report()
