"""Generate simple engagement metrics using PulseSync."""
from whirlcontrol import whirl_list, pulse_sync


def run_demo():
    crm = whirl_list.WhirlList()
    crm.add_member("Alice", "alice@example.com", tags=["pulse_active"])
    crm.add_member("Bob", "bob@example.com", tags=["pulse_active"])
    pulse_sync.record_pulse_response(crm, "bob@example.com")
    metrics = pulse_sync.summary_metrics(crm)
    print("Metrics:", metrics)


if __name__ == "__main__":
    run_demo()
