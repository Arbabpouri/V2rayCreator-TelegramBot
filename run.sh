#!/bin/bash

# Set the path to the Python script
PYTHON_SCRIPT="/path/to/python/script.py"

while true; do

    # Check if the Python script is running
    if ! pgrep -f "python $PYTHON_SCRIPT" >/dev/null; then
        # If the Python script is not running, start it
        echo "Starting Python script..."
        python $PYTHON_SCRIPT &
    fi

    # Wait for 5 minutes before checking again
    sleep 300
done