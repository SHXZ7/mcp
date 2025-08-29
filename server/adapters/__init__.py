from .noop import NoOpAdapter
from .http_adapter import HttpAdapter
from .git_adapter import GitAdapter
from .db_adapter import DbAdapter
from .http_tool_adapter import HttpToolAdapter
from .process_adapter import ProcessAdapter

adapters = {
    "noop": NoOpAdapter(),
    "http": HttpAdapter(),
    "git/status": GitAdapter(),
    "git/branches": GitAdapter(),
    "git/logs": GitAdapter(),
    "db/query": DbAdapter(),
    "http/get": HttpToolAdapter(),
    "http/post": HttpToolAdapter(),
    "process/run": ProcessAdapter()
}
