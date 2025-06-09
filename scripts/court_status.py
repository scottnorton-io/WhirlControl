"""Script to demonstrate updating court statuses."""

from whirlcontrol import court_signal


def display_status(grid):
    for label, status in grid.items():
        print(f"Court {label}: {status.value}")


def run_demo():
    grid = court_signal.get_court_grid()
    print("Initial status:")
    display_status(grid)
    # update one court
    court_signal.update_court_status(grid, "A", court_signal.CourtStatus.CAPACITY)
    print("\nAfter update:")
    display_status(grid)


if __name__ == "__main__":
    run_demo()
