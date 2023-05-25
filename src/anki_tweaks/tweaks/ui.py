import re

from aqt import QApplication, QWidget, mw, gui_hooks
from aqt.editor import Editor
from aqt.reviewer import ReviewerBottomBar
from aqt.webview import WebContent

from ..utils import config


# TODO: those are a bit tricky. Need to test carefully
# def set_webview_font(webview: AnkiWebView):
#     font_family = config.data["ui"]["font_family"]
#
#     webview.eval(f"""
#         document.body.style.fontFamily = '{font_family}'
#     """)
# def set_editor_webview_font(webview: EditorWebView):
#     font_family = config.data["ui"]["font_family"]
#
#     webview.eval(f"""
#         document.body.style.fontFamily = '{font_family}'
#     """)
# gui_hooks.webview_did_inject_style_into_page.append(set_webview_font)
# gui_hooks.editor_web_view_did_init.append(set_editor_webview_font)
# for w in QApplication.allWidgets():
#     w.setFont(font)
#     logger.debug(w.__class__.__name__)


def change_ui_global_font():
    """ Change application font globally

    NOTE: might also modify review/preview font for some fields
    """
    font_family = config.data["ui_font_family"]
    font_size = config.data["ui_font_size"]

    font = QApplication.font()
    font.setFamily(font_family)
    font.setPixelSize(font_size)

    QApplication.setFont(font)


def toggle_widget_text_visibility(widget: QWidget):
    """Try to hide element, preserving layout"""

    curr_style = widget.styleSheet()

    if re.match(r".*color: rgba\(0,0,0,0\).*", curr_style):
        widget.setStyleSheet(re.sub(r"color: rgba\(0,0,0,0\);?", "", curr_style))
    else:
        widget.setStyleSheet(curr_style + "; color: rgba(0,0,0,0)")


def toggle_review_widgets_on_state_change(new_state: str, old_state: str):
    """Show/hide review UI components"""

    if new_state == "review":
        # mw.mainLayout.removeWidget(mw.reviewer.bottom.web)
        # mw.reviewer.bottom.web.hide()
        toggle_widget_text_visibility(mw.menuBar())
        mw.toolbar.web.hide_while_preserving_layout()
    elif old_state == "review":
        toggle_widget_text_visibility(mw.menuBar())
        mw.toolbar.web.show()


def on_webview_will_set_content(web_content: WebContent, context):
    if isinstance(context, ReviewerBottomBar):
        if config.data["ui_clean_review"]:
            # Hide 'Edit', 'More' and 'Easy' buttons during review
            web_content.head += """<style>
                #innertable td[align='start'] button, #innertable td[align='end'] button { opacity: 0 }
                button[data-ease='4'] { display: none }
            </style>"""

    if isinstance(context, Editor):
        if config.data["ui_hide_hypertts_buttons_in_add_window"]:
            # Hide HyperTTS buttons in "add note" window
            web_content.head += """<style>
                .editor-toolbar #hypertts { display: none }
            </style>"""


def init_ui_tweak():
    gui_hooks.webview_will_set_content.append(on_webview_will_set_content)
    change_ui_global_font()

    if config.data["ui_clean_review"]:
        gui_hooks.state_did_change.append(toggle_review_widgets_on_state_change)


def update_ui_tweak():
    if config.data["ui_clean_review"]:
        gui_hooks.state_did_change.append(toggle_review_widgets_on_state_change)
    else:
        gui_hooks.state_did_change.remove(toggle_review_widgets_on_state_change)

    change_ui_global_font()
