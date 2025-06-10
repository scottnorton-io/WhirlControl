"""Demo exporting and loading SpinBoard moments as Markdown."""
from whirlcontrol import spin_board


def run_demo():
    board = spin_board.SpinBoard()
    board.add_moment("Kickoff", "Opening night was a blast!")
    board.add_moment("Shoutout", "Thanks to our volunteers.")
    md = board.to_markdown()
    print("Markdown Export:\n", md)

    loaded = spin_board.SpinBoard.from_markdown(md)
    for moment in loaded.list_moments():
        print(f"Loaded {moment.title} -> {moment.description}")


if __name__ == "__main__":
    run_demo()
