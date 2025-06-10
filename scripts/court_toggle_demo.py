"""Demo toggling court statuses using CourtSignal helpers."""
from whirlcontrol import court_signal


def run_demo():
    grid = court_signal.get_court_grid()
    for i in range(4):
        court_signal.toggle_court_status(grid, "A")
        status = grid["A"].value
        print(f"Toggle {i+1}: Court A -> {status}")


if __name__ == "__main__":
    run_demo()
