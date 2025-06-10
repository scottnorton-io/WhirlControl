"""Minimal Airtable helpers for WhirlControl.

These are placeholder functions representing how the system could
sync RSVP and pulse data to Airtable. They just print actions for now.
"""

from typing import Dict, Optional, List

# In-memory store to mimic Airtable table
_AIRTABLE_DB: Dict[str, Dict[str, str]] = {}


def update_airtable_record(email: str, fields: Dict[str, str]) -> None:
    """Update or create an Airtable record identified by email."""
    record = _AIRTABLE_DB.get(email, {"email": email})
    record.update(fields)
    _AIRTABLE_DB[email] = record
    print(f"[airtable] update {email} with {fields}")


def get_airtable_record(email: str) -> Optional[Dict[str, str]]:
    """Return a record if present in the in-memory table."""
    return _AIRTABLE_DB.get(email)


def list_airtable_records() -> List[Dict[str, str]]:
    """Return all stored records."""
    return list(_AIRTABLE_DB.values())
