BIN=.venv/bin/

init:
	# Make directory for Python venv
	python3 -m venv .venv

	# Install dependencies in virtual environment
	$(BIN)pip3 install -r requirements.txt

	# Done

run_example_all: run_example_fitting_a_curve run_example_get_bias_from_raw run_example_merge_cols_from_mutiple_csv_into_one_csv

run_example_fitting_a_curve:
	$(BIN)python3 -m usage_example.fitting_a_curve

run_example_get_bias_from_raw:
	$(BIN)python3 -m usage_example.get_bias_from_raw

run_example_merge_cols_from_mutiple_csv_into_one_csv:
	$(BIN)python3 -m usage_example.merge_cols_from_mutiple_csv_into_one_csv