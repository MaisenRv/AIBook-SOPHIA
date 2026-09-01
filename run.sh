#!/bin/bash
set -e
source ./venv/bin/activate
make html
sphinx-autobuild source build/html
