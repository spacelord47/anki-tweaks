import logging
import os
import sys

# TODO:
#   - use different colors for different levels

logger = logging.getLogger("AnkiTweaks")

if "ANKI_TWEAKS_DEBUG" in os.environ:
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.WARNING)


formatter = logging.Formatter(
    # fmt='[%(levelname)s](%(asctime)s) "%(pathname)s": line %(lineno)d: %(funcName)s: "%(message)s"',
    fmt="\x1b[33;20m{asctime} [{levelname}] {filename} | {funcName}\x1b[0m: {message}",
    datefmt="%d-%m-%y %H:%M:%S",
    style="{"
)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)

logger.addHandler(ch)
