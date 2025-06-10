"""Demo script for RecJamFeed module."""
from whirlcontrol import recjam_feed


def show_feed():
    feed = recjam_feed.RecJamFeed()
    feed.add_item("Jam Session 1", "https://example.com/jam1")
    feed.add_item("Jam Session 2", "https://example.com/jam2")
    for item in feed.list_items():
        print(f"{item.title} -> {item.link}")


if __name__ == "__main__":
    show_feed()
