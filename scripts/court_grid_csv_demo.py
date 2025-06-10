"""Demo exporting and loading court grid as CSV."""
from whirlcontrol import court_signal


def run_demo():
    grid = court_signal.get_court_grid()
    csv_data = court_signal.grid_to_csv(grid)
    print("CSV Export:\n", csv_data)

    loaded = court_signal.grid_from_csv(csv_data)
    for label, status in loaded.items():
        print(f"Court {label} -> {status.value}")


if __name__ == "__main__":
    run_demo()
