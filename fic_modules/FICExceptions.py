from fic_modules.configuration import (
    LOGGER
)


class FICExceptions():
    def __init__(self, error):
        self.e = int(error)

    def handle_exception(self):
        if self.e == 301:
            LOGGER.critical("Error code 301: Not Modified")
            exit(301)

        elif self.e == 302:
            LOGGER.critical("Error code 302: Found")
            exit(302)

        elif self.e == 304:
            LOGGER.critical("Error code 301: Not Modified")
            exit(304)

        elif self.e == 307:
            LOGGER.critical("Error code 307: Temporary Redirect")
            exit(307)

        elif self.e == 400:
            LOGGER.critical("Error code 400: Bad Request error")
            exit(400)

        elif self.e == 401:
            LOGGER.critical("Error code 401: Unauthorized error")
            exit(401)

        elif self.e == 403:
            LOGGER.critical("Error code 403: Forbidden error")
            exit(403)

        elif self.e == 404:
            LOGGER.critical("Error code 404: Not Found")
            exit(404)

        elif self.e == 422:
            LOGGER.critical("Error code 422: Unprocessable Entity")
            exit(422)

        elif self.e == 500:
            LOGGER.critical("Error code 500: Internal Server Error")
            exit(500)

        elif self.e == 501:
            LOGGER.critical("Error code 501: Not implemented")
            exit(501)

        elif self.e == 503:
            LOGGER.critical("Error code 503: Service Unavailable")
            exit(503)
