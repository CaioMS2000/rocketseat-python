class HTTPResponse:
    def __init__(
        self, body: dict | None = None, status_code: int = 200, headers: dict | None = None
    ):
        self.body = body
        self.status_code = status_code
        self.headers = headers
