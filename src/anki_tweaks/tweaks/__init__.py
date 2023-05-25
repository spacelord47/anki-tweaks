from .cloze import init_cloze_tweak, update_cloze_tweak
from .nav import init_nav_tweak, update_nav_tweak
from .template_editor import init_template_editor_tweak, update_template_editor_tweak
from .ui import init_ui_tweak, update_ui_tweak
from ..utils import config


def init_tweaks():
    init_nav_tweak()

    if config.data["template_editor__enabled"]:
        init_template_editor_tweak()
    if config.data["ui__enabled"]:
        init_ui_tweak()
    if config.data["cloze__enabled"]:
        init_cloze_tweak()


def update_tweaks():
    update_nav_tweak()

    if config.data["template_editor__enabled"]:
        update_template_editor_tweak()
    if config.data["ui__enabled"]:
        update_ui_tweak()
    if config.data["cloze__enabled"]:
        update_cloze_tweak()


config.config_update_cb.append(update_tweaks)
