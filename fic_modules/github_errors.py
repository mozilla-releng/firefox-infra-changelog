from fic_modules.configuration import (
    LOGGER
)


def handle_301():
    LOGGER.info("Moved Permanently")
    exit(0)


def handle_302():
    LOGGER.info("Found")
    exit(0)


def handle_304():
    LOGGER.info("Not Modified")
    exit(0)


def handle_307():
    LOGGER.info("Temporary Redirect")
    exit(0)


def handle_400():
    LOGGER.info("Bad Request error")
    exit(0)


def handle_401():
    LOGGER.info("Unauthorized error")
    exit(0)


def handle_403():
    LOGGER.info("Forbidden error")
    exit(0)


def handle_404():
    LOGGER.info("Not Found")
    exit(0)


def handle_422():
    LOGGER.info("Unprocessable Entity")
    exit(0)


def handle_500():
    LOGGER.info("Internal Server Error")
    exit(0)


def handle_501():
    LOGGER.info("Not implemented")
    exit(0)


def handle_503():
    LOGGER.info("Service Unavailable")
    exit(0)
