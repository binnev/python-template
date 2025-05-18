# How to Build Documentation

This guide explains how to build the documentation for the project.

## Steps

1. Install MkDocs and its dependencies:
    ```sh
    uv pip install -r pyproject.toml --all-extras
    ```

2. Serve the documentation locally:
    ```sh
    mkdocs serve
    ```

3. Build the documentation:
    ```sh
    mkdocs build
    ```

The built documentation will be available in the `site/` directory.