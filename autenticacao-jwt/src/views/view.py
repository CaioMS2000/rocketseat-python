from abc import ABC, abstractmethod
from .http_types import HTTPRequest, HTTPResponse


class View(ABC):
    @abstractmethod
    def handler(self, request: HTTPRequest) -> HTTPResponse: ...
