# Python project template 

## Dependency management 
Use `uv` -- it's basically a Cargo for python, written in rust


Add a dependency: 
```sh
uv add ruff
```

Add a dependency to the optional "dev" group: 
```sh
uv add ruff --optional dev
```

Create a new lockfile: 
```sh 
uv lock 
```

Pass `--upgrade` to upgrade: 
```sh 
uv lock --upgrade
```

Install dependencies:  
(this will only install the core dependencies)
```sh 
uv pip install -r pyproject.toml
```

Install extra dependencies defined in `project.optional-dependencies`:  
```sh 
uv pip install -r pyproject.toml --all-extras
```

## Tests 

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