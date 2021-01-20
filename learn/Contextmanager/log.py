from contextlib import contextmanager
import logging


@contextmanager
def log(level):
    logger = logging.getLogger()
    current_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield
    finally:
        logger.setLevel(current_level)


def some_func():
    logging.debug("Some debug level information...")
    logging.error("Serious error...")
    logging.warning("Some warning messages...")


with log(logging.DEBUG):
    some_func()
