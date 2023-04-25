import logging


def setup_logger():
    logger = logging.getLogger('application')
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '%(asctime)s - %(module)s.%(funcName)s - %(levelname)s - %(message)s'
    )
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


def camel_case_to_snake_case(s):
    return ''.join(['_' + c.lower() if c.isupper() else c for c in s]).lstrip('_')


def snake_case_to_camel_case(s):
    return ''.join([c.capitalize() for c in s.split('_')])
