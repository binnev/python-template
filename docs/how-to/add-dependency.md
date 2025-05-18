# How to Add a Dependency

This guide explains how to add a new dependency to the project.

## Steps

1. Add the dependency using `uv`:
    ```sh
    uv add <dependency-name>
    ```

2. If the dependency is for development purposes, add it to the `dev` group:
    ```sh
    uv add <dependency-name> --optional dev
    ```

3. Update the lockfile:
    ```sh
    uv lock
    ```

4. Install the updated dependencies:
    ```sh
    uv pip install -r pyproject.toml --all-extras
    ```