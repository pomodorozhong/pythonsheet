# pythonsheet

A tool for basic spreadsheet workflow.

## To Install Dependencies

### OS X & Linux

using `make`

```sh
make init
```

or

```sh
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

## To Run Examples

### Using `make`

The general form of command is `make run_example_<example_name>`.

like this:

```sh
make run_example_fitting_a_curve
```

or run it all

```sh
make run_example_all
```

### Use Python directly

```sh
cd root/path/of/this/repo
python3 -m usage_exaple.fitting_a_curve
```
