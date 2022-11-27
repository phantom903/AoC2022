set shell := ["powershell.exe", "-c"]

# Lists available recipes
@menu:
    just --list --unsorted

# Creates a folder for a given day's problem
@setup day:
    python problem_setup.py {{day}}
    echo "Day {{day}} setup. Good luck!"

# Removes a given day's folder
@remove day:
    rm -rf day_$(printf %02d {{day}})
    echo "Day {{day}} removed."

# Removes and re-creates a given day's folder
@reset day: (remove day) (setup day)

# Runs the specified part of the specified problem using sample input, with log level set to DEBUG
@debug day part:
    python problem_runner.py {{day}} check {{part}} --log-level DEBUG

# Runs the specified part of the specified problem using sample input
@check day part:
    python problem_runner.py {{day}} check {{part}}

# Runs the specified part of the specified problem using full input
@solve day part:
    python problem_runner.py {{day}} solve {{part}}

# Shows what changes Black would make
@black-check:
    python -m black --diff .

# Runs Black on all files in this folder and subfolders
@black:
    python -m black .

# Runs Pytest on the specified problem
@test day:
    pytest day_$(printf %02d {{day}})

# Runs all tests
@test-all:
    pytest --ignore templates

# Runs a timed execution of all regestered complete problems
@benchmark:
    python problem_runner.py

# Creates config-secret.toml
@init-secret-config:
    echo '[auth]\ncookie = ""' > config_secret.toml
