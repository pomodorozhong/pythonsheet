#!/bin/bash

# Save original working directory
origin_wd=$(pwd)

# Change directory to the root of the repo
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"
cd ..

# Make directory to store input/output file.
mkdir in
mkdir out
mkdir out/plot

# Reset working directory
cd "$origin_wd"
