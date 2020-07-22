#!/bin/bash

# Save original working directory
origin_wd=$(pwd)

# Change directory to the root of the repo
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"
cd ..

# Make directory to store input/output file.
mkdir in
mkdir out/plot

# Make directory for Python venv
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip3 install -r requirements.txt

# Reset working directory
cd "$origin_wd"
