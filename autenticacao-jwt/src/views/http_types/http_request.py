class HTTPRequest:
    def __init__(
        self,
        body: dict | None = None,
        headers: dict | None = None,
        query_params: dict | None = None,
        tokens: dict | None = None,
    ):
        self.body = body
        self.headers = headers
        self.query_params = query_params
        self.tokens = tokens
