# Tasks For My Project


<!-- A heading defines the command's name -->
## build

<!-- A blockquote defines the command's description -->
> Builds my project

<!-- A code block defines the script to be executed -->
```sh
echo "building project..."
```


## test

> Run all the tests


```sh
pytest -n 6
```

## docs-live 

> Hot-reload the documentation with `mkdocs`

```sh
mkdocs serve 
```

## bump

> Create a new version of the project, docs, and changelog 

```sh
cz bump 
git-cliff -o CHANGELOG.md
mike deploy $(cz version --project) latest --update-aliases
```