from aqt import gui_hooks, mw

from ..utils import config


def move_to_deck_browser_after_review(new_state: str, old_state: str):
    """Redirect to deck browser(instead of deck overview) after finishing deck review

    TODO: implement check for is deck finished for today
    """
    if old_state == "review" and new_state == "overview":
        mw.moveToState("deckBrowser")


def init_nav_tweak():
    if config.data["nav_skip_review_congratulations"]:
        gui_hooks.state_did_change.append(move_to_deck_browser_after_review)


def update_nav_tweak():
    if config.data["nav_skip_review_congratulations"]:
        gui_hooks.state_did_change.append(move_to_deck_browser_after_review)
    else:
        gui_hooks.state_did_change.remove(move_to_deck_browser_after_review)
