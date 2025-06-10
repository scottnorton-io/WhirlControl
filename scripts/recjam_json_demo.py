"""Demo exporting and loading RecJam feed items as JSON."""
from whirlcontrol import recjam_feed


def run_demo():
    feed = recjam_feed.RecJamFeed()
    feed.add_item("Jam 1", "https://example.com/1")
    feed.add_item("Jam 2", "https://example.com/2")
    data = feed.to_json()
    print("JSON Export:\n", data)

    loaded = recjam_feed.RecJamFeed.from_json(data)
    for item in loaded.list_items():
        print(f"Loaded {item.title} -> {item.link}")


if __name__ == "__main__":
    run_demo()
