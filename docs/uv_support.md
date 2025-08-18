# UV Support

This repository now supports using [uv](https://github.com/astral-sh/uv) as an alternative package manager for faster dependency installation.

## What is UV?

uv is an extremely fast Python package installer and resolver, written in Rust. It can significantly speed up the installation of dependencies compared to traditional pip.

## How to Use UV

To use uv instead of pip for package installation, simply add the `--use-uv` flag when launching the webui:

```bash
# On Windows
webui.bat --use-uv

# On Linux/macOS
./webui.sh --use-uv

# Or directly with Python
python launch.py --use-uv
```

## How It Works

When the `--use-uv` flag is provided:

1. The system first checks if uv is installed
2. If uv is not available, it will automatically install it using pip
3. Virtual environment creation uses `uv venv` instead of `python -m venv` (Windows only)
4. All subsequent package installations will use uv instead of pip
5. If for any reason uv fails, the system will fall back to pip

## Benefits

- **Faster Installation**: uv can install packages significantly faster than pip
- **Faster Virtual Environment Creation**: uv creates virtual environments much faster than the standard venv module
- **Automatic Fallback**: If uv is not available or fails, the system automatically falls back to pip
- **No Configuration Required**: Simply add the flag and the system handles the rest

## Requirements

- Python 3.10 or higher (Python 3.11 or 3.12 recommended)
- Internet connection (for initial uv installation if not present)

## Notes

- UV support is completely optional - the default behavior (using pip) remains unchanged
- All existing functionality and command-line arguments continue to work as before
- UV is only used for package installation and virtual environment creation, not for running the application itself
- Python 3.13 support is experimental and may have issues with some packages