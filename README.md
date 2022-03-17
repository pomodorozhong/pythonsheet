# pythonsheet

A tool for basic spreadsheet workflow.

Most of it is a wrapper of `numpy` and `pandas`, plus some random text processing.

## Requirements

Besides `requirements.txt`, the Python version needs to be `3.8`.

- `3.8` works, tested on 2022-03-17.
- `3.10` fails, tested on 2022-03-17.

Other Python version is not tested.

## Installation

### OS X & Linux

```sh
cd root/path/of/this/repo

python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

or using `make` to do above

```sh
make init
```

### Windows

```cmd
cd root\path\of\this\repo

python3 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip3 install -r requirements.txt
```

If you encounter errors when `.\.venv\Scripts\Activate.ps1`, try run `Set-ExecutionPolicy -ExecutionPolicy Unrestricted` as administrator in Powershell before doing it.

## Run Usage Examples

### Use Python directly

```sh
cd root/path/of/this/repo
python3 -m usage_exaple.fitting_a_curve
```

### Using `make`

The general form of command is `make run_example_<example_name>`. like this:

```sh
make run_example_fitting_a_curve
```

And to run it all by `run_example_all`:

```sh
make run_example_all
```
