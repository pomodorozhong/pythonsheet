# pythonsheet

A tool for basic spreadsheet workflow.

Most of it is a wrapper of `numpy` and `pandas`, plus some random text processing.

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
