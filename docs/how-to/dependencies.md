# Dependency management 
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
