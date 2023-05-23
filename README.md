# Screener

Check e-book files for security and privacy issues.

_Screener is currently in early development. Please consider contributing if you have the time and know-how!_

## Motivation

E-books are great, but the common file formats have security and privacy issues. Most use web browser technologies like HTML, CSS, and JavaScript. Therefore, e-books are vulnerable to security and privacy issues that already exist on the web.

Screener aims to check e-book files for these issues so that you can read with peace of mind!

## Features

- Check e-book files for JavaScript tags.
- Check e-book files for images with external sources to prevent tracking.
- Supports `.epub`, `.mobi`, and `.azw3` files.

## Get started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Screener requires [Python](https://www.python.org/about/gettingstarted/) (version 3.10 or newer).

### Installing

Screen is available on [PyPI](https://pypi.org/project/screener/). To install, run:

```bash
pip install screener
```

#### Development installation

To install Screener for development, clone the repository and run:

```bash
poetry install
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

At present, this project is in early development and needs extra security and privacy checks and wider file format support more than anything else.

Please make sure to update tests as appropriate.

## Versioning

This project uses [SemVer](http://semver.org/) for versioning.

## Authors

Screener was created by Tom Kuson ([@tjkuson](https://github.com/tjkuson)).

## Licence

Screener is released under the [LGPL version 3](LICENCE).
