from .noop import NoOpAdapter
from .http_adapter import HttpAdapter

adapters = {
    "noop": NoOpAdapter(),
    "http": HttpAdapter()
}
