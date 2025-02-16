# hog

## Description
`hog` is a Python script that progressively allocates memory in chunks until nearly all system memory is consumed. This can be useful for testing system behavior under low-memory conditions.

## Requirements
- Python 3.x
- `psutil` package (installed automatically in the virtual environment)

## Setup
A Python virtual environment is provided in the `/venv` directory. To activate it:

### On Windows (Command Prompt or PowerShell):
```
venv\Scripts\activate
```

### On Linux/macOS:
```
source venv/bin/activate
```

Ensure dependencies are installed:
```
pip install -r requirements.txt
```

## Usage
Run the script with:
```
python hog.py
```
By default, it allocates 100MB every 0.5 seconds. Modify `step_mb` or `sleep_time` in the script to adjust behavior.

## Building with Nuitka
To compile the script into a standalone executable using Nuitka, run the following command:
```
./build.cmd
```
This will use Nuitka to package the script along with required dependencies.

## Warning
This script will consume nearly all available memory on your system. Use with caution, as it may cause system instability or crashes.

