# Project tasks
Mask is a modern markdown-based replacement for `make` and `Makefile`. The code blocks defined in this file are runnable via the `mask` CLI (try `mask --help`), and the surrounding markdown serves as the documentation.

See the docs: https://github.com/jacobdeichert/mask


<!-- A heading defines the command's name -->
## test

<!-- A blockquote defines the command's description -->
> Run all the tests

<!-- A code block defines the script to be executed -->
```sh
pytest -n 6
```

## docs

> Hot-reload the documentation with `mkdocs`

```sh
mkdocs serve 
```

### docs bump 

> Create a new version of the docs

```sh 
mike deploy $(cz version --project) latest --update-aliases
mike set-default latest
```

## bump

> Create a new version of the project, docs, and changelog 

```sh
git-cliff -o changelog --bump \
&& cz bump \
    && mask docs bump
```

## changelog 

> Update the changelog with `git-cliff`

```sh
git-cliff -o CHANGELOG.md
```

Positional arguments

These are defined beside the command name within (round_brackets). They are required arguments that must be supplied for the command to run. The argument name is injected into the script's scope as an environment variable.

Example:

## pos (file) (test_case)

> Positional args example

~~~bash
echo "Testing $test_case in $file"
~~~

Optional arguments are defined within [square_brackets].

Example:

## opt [test_file]

> Optional args example

~~~bash
if [[ -n "$test_file" ]]; then
    echo "Run tests in $test_file..."
else
    echo "Running all tests...."
fi
~~~