"""Utility helpers to simulate Mailchimp actions."""

from typing import Iterable


def tag_mailchimp(email: str, tag: str) -> None:
    """Placeholder to tag a Mailchimp contact."""
    print(f"[mailchimp] tag {email} with {tag}")


def send_mailchimp_template(email: str, template: str) -> None:
    """Placeholder to send a Mailchimp template."""
    print(f"[mailchimp] send template '{template}' to {email}")


def send_bulk_template(emails: Iterable[str], template: str) -> None:
    """Send the given template to each email in ``emails``."""
    for email in emails:
        send_mailchimp_template(email, template)
