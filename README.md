# Screener

Check e-book files for security and privacy issues.

## Motivation

E-books are great, but the common file formats have security and privacy issues.
Most use web browser technologies like HTML, CSS, and JavaScript. Therefore,
e-books are vulnerable to security and privacy issues that already exist on the
web.

Screener aims to check e-book files for these issues so that you can read with
peace of mind!

## Features

- Check e-book files for JavaScript tags.
- Check e-book files for images with external sources to prevent tracking.
- Supports `.epub`, `.mobi`, and `.azw3` files.

## Get started

Screener is available on [PyPI](https://pypi.org/project/screener/). To install,
run

```bash
pip install screener
```

### Usage

To check a file, try:

```shell
screener path/to/file.epub
```

For help:

```shell
screener --help
```

## Contributing

Pull requests are welcome and appreciated. For major changes, please open an
issue first to discuss what you would like to change. Please make sure to update
tests as appropriate.

If you have found a bug or have a feature request, please open an issue.
