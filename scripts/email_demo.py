"""Demo using email utilities to tag and send templates."""

from whirlcontrol import email_utils


def run():
    email_utils.tag_mailchimp("demo@example.com", "core_crew")
    email_utils.send_mailchimp_template("demo@example.com", "welcome")


if __name__ == "__main__":
    run()

