"""Demo script for SpinBoard module."""
from whirlcontrol import spin_board


def show_spinboard():
    board = spin_board.SpinBoard()
    board.add_moment("First Match", "Kicked off the season with a full house!")
    board.add_moment("Community Shoutout", "Thanks to our volunteers this week.")
    for moment in board.list_moments():
        print(f"{moment.title}: {moment.description}")


if __name__ == "__main__":
    show_spinboard()
