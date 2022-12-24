# python-app-template

This is a template for a Python project.

The following following tools have been configured:

- [poetry](https://python-poetry.org) for dependency management
- [black](https://github.com/psf/black) for code formatting
- [mypy](http://mypy-lang.org) for static type checking
- [isort](https://github.com/PyCQA/isort) for sorting imports
- [flake8](https://flake8.pycqa.org) for linting
- [pylint](https://www.pylint.org) for linting
- [bandit](https://github.com/PyCQA/bandit) for security linting
- [poethepoet](https://github.com/nat-n/poethepoet) for running the above tools
- [unittest](https://docs.python.org/3/library/unittest.html) for unit testing

## Usage

The project uses [poetry](https://python-poetry.org), you can install it with:

```bash
pip install poetry
```

### Install dependencies

```bash
poetry install
```

### Edit the code

You can edit the code in the `python_app_template` directory.

### Test the application

The tests can be found in the `test` directory.
[unittest](https://docs.python.org/3/library/unittest.html) is used for unit testing.

To run the tests:

```bash
poetry run poe unittest-check
```

### Run the linter

```bash
poetry run poe linting-check
```

Note: The linter will return a non-zero exit code if there are any linting errors or warnings.

### Run the formatter

```bash
poetry run poe formatting-check
```

Formatting errors can be automatically fixed by running:

```bash
poetry run poe formatting-fix
```

## CI Pipeline

The CI pipeline is configured in the `.github/workflows/ci.yml` file.
