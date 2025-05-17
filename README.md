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
