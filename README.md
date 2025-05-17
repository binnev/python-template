# Python project template 

## Dependency management 
Use `uv` -- it's basically a Cargo for python, written in rust


Add a library: 
```sh
uv add ruff
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

