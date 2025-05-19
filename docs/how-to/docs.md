# Docs

## View the documentation locally:
Run: 
```sh
mkdocs serve
```
and go to `localhost:8000` to view the docs. Mkdocs hot-reloads the docs, so any changes you make will be immediately visible.


## Versioning 
We use `mike` to manage versioning for our documentation. It creates a snapshot of the documentation for each version of the project, allowing users to access the appropriate docs for the version they're using—even if it's an older one.

### Build new docs version 
Build the docs for the current project version: 
```sh 
mike deploy $(cz version --project)
```

Alias the new version of the docs to "latest" and set that as the default docs version.
```sh
mike alias $(cz version --project) latest
mike set-default latest
```
