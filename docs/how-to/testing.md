# Tests 

Running all tests should be as simple as this, if everything is configured
correctly in the `pyproject.toml`
```sh
pytest
```

To automatically re-run tests while you are working on them, use
[`pytest-watcher`](https://github.com/olzhasar/pytest-watcher) (`q` to quit):
```sh
ptw .
```