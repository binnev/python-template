# Project Structure

This document explains the structure of the Python Template project.

## Overview

The project is organized as follows:

```
python-template/
├── cli/                # Command-line interface
│   ├── __init__.py
│   ├── __main__.py
│   └── calculator.py
├── core/               # Core functionality
│   ├── __init__.py
│   └── calculator.py
├── tests/              # Unit tests
│   ├── __init__.py
│   ├── test_calculator.py
│   └── test_async_stuff.py
├── docs/               # Documentation
│   └── index.md
├── main.py             # Entry point
├── pyproject.toml      # Project configuration
└── README.md           # Project overview
```

## Key Components

- **CLI:** Provides a command-line interface using `typer`.
- **Core:** Contains the core logic for the calculator.
- **Tests:** Includes unit tests for the project.
- **Docs:** Contains documentation files for the project.