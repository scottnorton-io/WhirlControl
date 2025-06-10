"""Demo exporting and loading court grid as JSON."""
from whirlcontrol import court_signal


def run_demo():
    grid = court_signal.get_court_grid()
    json_data = court_signal.grid_to_json(grid)
    print("JSON Export:\n", json_data)

    loaded = court_signal.grid_from_json(json_data)
    for label, status in loaded.items():
        print(f"Court {label} -> {status.value}")


if __name__ == "__main__":
    run_demo()
