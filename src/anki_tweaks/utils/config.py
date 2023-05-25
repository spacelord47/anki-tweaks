from aqt import mw

data: dict = {}
addon_package: str = ""
config_update_cb = []


def on_config_update(updated_config):
    global data
    data = updated_config

    for cb in config_update_cb:
        cb()


# TODO: check and remove old keys from JSON on startup
def init(_root_package: str):
    global data
    global addon_package

    data = mw.addonManager.getConfig(_root_package)
    addon_package = _root_package

    mw.addonManager.setConfigUpdatedAction(addon_package, on_config_update)
    mw.addonManager.setWebExports(addon_package, r"assets/.*(css|js)")
