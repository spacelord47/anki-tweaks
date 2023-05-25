from aqt import gui_hooks
from aqt.clayout import CardLayout

from ..utils import config


def set_template_editor_font(card_layout: CardLayout):
    font_family = config.data["template_editor_font_family"]
    font_size = config.data["template_editor_font_size"]

    font = card_layout.tform.edit_area.font()
    font.setFamily(font_family)
    font.setPixelSize(font_size)

    card_layout.tform.edit_area.setFont(font)


def init_template_editor_tweak():
    gui_hooks.card_layout_will_show.append(set_template_editor_font)


def update_template_editor_tweak():
    pass
