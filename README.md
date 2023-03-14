# Screener
[![Codacy](https://img.shields.io/codacy/grade/d21e502c643442ff88b493ad11470c4d)](https://app.codacy.com/gh/tjkuson/screener/dashboard?branch=main)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Check e-book files for security and privacy issues.

*Screener is currently in early development. Please consider contributing if you have the time and know-how!*

## Motivation

E-books are great, but the common file formats have security and privacy issues. Most use web browser technologies like 
HTML, CSS, and JavaScript. Therefore, e-books are vulnerable to security and privacy issues that already exist on the 
web.

Screener aims to check e-book files for these issues so that you can read with peace of mind!

## Features

-   Check e-book files for JavaScript tags.
-   Supports `.epub` and `.azw3` files.

## Get started

These instructions will get you a copy of the project up and running on your local machine for development and testing
purposes.

### Prerequisites

Screener requires [Python](https://www.python.org/about/gettingstarted/) (version 3.10 is recommended), 
[pip](https://pip.pypa.io/en/stable/getting-started/), and [Poetry](https://python-poetry.org/docs/#installation) to 
be installed.

### Installing

Copy the files in this repository and navigate to the repository directory. You can run the project with `poetry run`.

```commandline
poetry run python screener/screener.py
```

You can also run tests.

```commandline
poetry run pytest
```

With coverage metrics:

```commandline
poetry run coverage run -m pytest
```

Type-checking:

```commandline
poetry run mypy screener/
```

This is the recommended way to install Screener for development and testing.

#### Alternative installation

If you would rather not use `poetry run`, you can use `poetry export` to create a `requirements.txt` file and install 
the packages directly using `pip`.

```commandline
poetry export -f requirements.txt --output requirements.txt
pip install -r requirements.txt
```

You can then use Python as normal.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

At present, this project is in early development and needs extra security and privacy checks and wider file format 
support more than anything else.

Please make sure to update tests as appropriate.

## Versioning

This project uses [SemVer](http://semver.org/) for versioning.

## Authors

Screener was created by Tom Kuson ([@tjkuson](https://github.com/tjkuson)).

## Licence

Screener is released under the [LGPL version 3](LICENCE).
