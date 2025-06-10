# WhirlControl

Minimal prototype implementing modules described in the build spec.
This version provides Python stubs representing core functionality. Modules can
be wired together in simple scripts to simulate RSVP and survey workflows.

## Quick Start
1. Install dependencies if needed.
2. Run the RSVP demo:
```bash
PYTHONPATH=. python scripts/rsvp_handler.py
```
This prints sample RSVP handling actions.


## Modules
- `court_signal` – static representation of court status
- `whirl_list` – in-memory CRM model
- `spin_board` – holder for shoutouts and moments
- `pulse_sync` – survey tracking helpers
- `popup_rsvp` – basic RSVP webhook handler
- `recjam_feed` – simple read-only feed model
- `email_utils` – placeholder Mailchimp actions
- `airtable_utils` – stub functions to mimic Airtable sync
  now stores records in memory for demos

## Recent additions
- `WhirlList` now supports JSON and CSV import/export plus tag filtering.
- `PulseSync.weekly_pulse_cycle` marks members as low engaged via tags and `summary_metrics` counts engagement.
- Added court status toggling utilities with `court_toggle_demo.py`.
- New demos cover SpinBoard, RecJamFeed, CSV helpers, and analytics snapshots.
- `airtable_utils` keeps an in-memory table and can list or delete records.
- `SpinBoard` can export and load moments from Markdown and JSON.
- `RecJamFeed` now supports JSON export/import.
- `RecJamFeed` can also export and import Markdown lists.
- `RecJamFeed` now supports CSV export/import.
- `court_signal` helpers serialize the grid to JSON and CSV.

Scripts showcase:

- `rsvp_handler.py` – simulates a Tally webhook storing RSVP info
- `pulse_reminder.py` – demonstrates a weekly pulse cycle with status output
- `court_status.py` – updates the court grid and prints results
- `spinboard_demo.py` – adds and lists SpinBoard moments
- `spinboard_markdown_demo.py` – exports moments to Markdown
- `spinboard_json_demo.py` – exports moments to JSON
- `recjam_demo.py` – shows a basic RecJam feed
- `recjam_json_demo.py` – exports feed items to JSON
- `recjam_markdown_demo.py` – exports feed items to Markdown
- `recjam_csv_demo.py` – exports feed items to CSV
- `whirl_list_json.py` – exports and loads CRM data as JSON
- `whirl_list_csv.py` – exports and loads CRM data as CSV
- `court_grid_json_demo.py` – exports and loads court grid as JSON
- `court_grid_csv_demo.py` – exports and loads court grid as CSV
- `court_toggle_demo.py` – cycles court statuses in place
- `summary_metrics_demo.py` – prints engagement metrics
- `email_demo.py` – shows tagging and email templates
- `airtable_demo.py` – demonstrates Airtable helpers with an in-memory record list and delete example

Example scripts live in the `scripts/` folder. Run them with `PYTHONPATH=. python scripts/<name>.py` to see sample output.
Analytics snapshots (pulse metrics) can be generated in `analytics/`.
