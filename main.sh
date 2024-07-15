#!/bin/sh

if [ "$(uname)" = "Darwin" ]; then
    PYTHON_PATH="/opt/homebrew/bin/python3"
elif [ "$(uname)" = "Linux" ]; then
    PYTHON_PATH="/usr/bin/python3"
elif [ "$(uname -o)" = "Cygwin" ] || [ "$(uname -o)" = "Msys" ]; then
    PYTHON_PATH="/c/Users/Stas/AppData/Local/Microsoft/WindowsApps/python3"
else
    echo "Unsupported operating system"
    exit 1
fi

$PYTHON_PATH main.py "$@"
