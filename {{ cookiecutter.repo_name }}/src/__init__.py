import sys

from loguru import logger

fmt = '{time:YYYY-MM-DD HH:mm:ss} | {level} | {name} :: {module} :: {function} :: {line} - {message}'

config = {
    "handlers": [
        {"sink": sys.stdout, 'level': "DEBUG"},
        {"sink": "log.log", "format": fmt, 'level': 'DEBUG'},
    ]
}

logger.configure(**config)