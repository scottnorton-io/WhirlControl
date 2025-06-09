# WhirlControl

Minimal prototype implementing modules described in the build spec.
This version provides Python stubs representing core functionality. Modules can
be wired together in simple scripts to simulate RSVP and survey workflows.

## Modules
- `court_signal` – static representation of court status
- `whirl_list` – in-memory CRM model
- `spin_board` – holder for shoutouts and moments
- `pulse_sync` – survey tracking helpers
- `popup_rsvp` – basic RSVP webhook handler
- `recjam_feed` – simple read-only feed model

## Recent additions
- `WhirlList` now supports JSON import/export and tag filtering.
- `PulseSync.weekly_pulse_cycle` marks members as low engaged via tags.
- Added `court_status.py` example script for court grid updates.

Scripts showcase:

- `rsvp_handler.py` – simulates a Tally webhook storing RSVP info
- `pulse_reminder.py` – demonstrates a weekly pulse cycle with status output
- `court_status.py` – updates the court grid and prints results

Example scripts live in the `scripts/` folder. Run them with `PYTHONPATH=. python
scripts/<name>.py` to see sample output.
