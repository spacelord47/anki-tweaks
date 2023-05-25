from typing import Any

from aqt import gui_hooks
from aqt.browser.previewer import BrowserPreviewer
from aqt.reviewer import Reviewer
from aqt.utils import tooltip
from aqt.webview import WebContent

from ..utils import config


def inject_cloze_assets(webview: WebContent, context):
    if isinstance(context, BrowserPreviewer) is False and isinstance(context, Reviewer) is False:
        return

    next_shortcut = config.data["cloze_shortcut_open_next"]
    all_shortcut = config.data["cloze_shortcut_open_all"]

    webview.head += (f"""
            <script>
                window.anki_tweaks = {{
                    next_shortcut: '{next_shortcut}',
                    all_shortcut: '{all_shortcut}',
                }};
            </script>
        """)

    webview.js.append(f"/_addons/{config.addon_package}/assets/js/cloze.js")


def handle_cloze_js_messages(handled: (bool, Any), msg: str, context: Any) -> tuple[bool, Any]:
    if msg == "anki_tweaks:cloze:no_more_hidden":
        tooltip("No hidden cloze", 1500)
        return True, None

    return handled


def init_cloze_tweak():
    gui_hooks.webview_will_set_content.append(inject_cloze_assets)
    gui_hooks.webview_did_receive_js_message.append(handle_cloze_js_messages)


def update_cloze_tweak():
    pass
