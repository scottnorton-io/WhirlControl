"""Demo exporting and loading SpinBoard moments as JSON."""
from whirlcontrol import spin_board


def run_demo():
    board = spin_board.SpinBoard()
    board.add_moment("Opening Day", "Courts packed with energy")
    board.add_moment("Volunteer Shoutout", "Big thanks to the crew")
    data = board.to_json()
    print("JSON Export:\n", data)

    loaded = spin_board.SpinBoard.from_json(data)
    for moment in loaded.list_moments():
        print(f"Loaded {moment.title} -> {moment.description}")


if __name__ == "__main__":
    run_demo()
