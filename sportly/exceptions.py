"""Custom exceptions for sportly."""


class SportlyError(Exception):
    """Base exception for all sportly errors."""

    def __init__(self, message: str, status_code: int | None = None, url: str | None = None):
        super().__init__(message)
        self.status_code = status_code
        self.url = url

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self!s})"


class NotFoundError(SportlyError):
    """Raised when the requested resource does not exist (HTTP 404)."""


class RateLimitError(SportlyError):
    """Raised when the upstream API rate-limits the request (HTTP 429)."""


class AuthenticationError(SportlyError):
    """Raised when authentication fails (HTTP 401/403)."""


class UpstreamError(SportlyError):
    """Raised for 5xx errors from upstream APIs."""


class ParseError(SportlyError):
    """Raised when a response cannot be parsed."""
