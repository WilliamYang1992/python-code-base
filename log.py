import logging
import sys
from logging.handlers import TimedRotatingFileHandler

FORMATTER = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
LOG_FILE = "app.log"


def get_console_handler(out=None):
    if not out:
        out = sys.stdout
    console_handler = logging.StreamHandler(out)
    console_handler.setFormatter(FORMATTER)
    return console_handler


def get_file_handler(log_file=None):
    if not log_file:
        log_file = LOG_FILE
    file_handler = TimedRotatingFileHandler(log_file, when='midnight')
    file_handler.setFormatter(FORMATTER)
    return file_handler


def get_logger(logger_name, log_level=None, handlers=None, filters=None):
    logger = get_logger_with_default_conf(logger_name, log_level)

    if handlers:
        for handler in handlers:
            logger.addHandler(handler)

    if filters:
        for filter in filters:
            logger.addFilter(filter)

    return logger


def get_logger_with_default_conf(logger_name, log_level=None):
    logger = logging.getLogger(logger_name)

    if not log_level:
        log_level = logging.DEBUG
    logger.setLevel(log_level)

    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())

    logger.propagate = False

    return logger
