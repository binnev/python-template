# Testing 

## Run all tests
Running all tests should be as simple as this:
```sh
pytest
```

## Run specific tests
Run only tests which have "foo" in the file or function name: 
```sh
pytest -k foo
```

## Watch tests
To automatically re-run tests while you are working on them, use 
[`pytest-watcher`](https://github.com/olzhasar/pytest-watcher) (`q` to quit):
```sh
ptw .
```

You can also watch specific tests using the `-k` flag: 
```sh 
ptw . -k foo 
```

By default, tests are re-run 0.2 seconds after the last file edit. To increase the delay, pass `--delay`: 
```sh 
ptw . --delay 5
```

## Getting test coverage 
### Terminal 
To see the test coverage, add `--cov` to any of the above commands. For example, this will output the coverage report to the terminal:
```sh 
pytest --cov
```

### HTML report
To see a browsable HTML report:
```sh 
pytest --cov --cov-report=html && xdg-open htmlcov/index.html
```

You can watch HTML coverage by running: 
```sh 
ptw . --cov --cov-report=html
```
and opening `htmlcov/index.html` in your browser. 

To watch coverage for a specific test: 
```sh 
ptw . -k foo --cov --cov-report=html
```
The tests may "fail" because the tests matching `foo` will be expected to provide coverage for the whole project. But you can open `htmlcov/index.html` in your browser and browse to just the relevant file. 