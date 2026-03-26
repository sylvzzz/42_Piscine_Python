"""
construct.py - The Matrix Virtual Environment Detector
Detects and displays information about the current Python environment.
"""

import os
import sys
import site


def get_virtual_env_path() -> str | None:
    """
    Detect if a virtual environment is active.

    Returns the path to the virtual environment if one is active,
    or None if running in the global environment.
    """
    # VIRTUAL_ENV is set by activate scripts (venv, virtualenv)
    virtual_env = os.environ.get("VIRTUAL_ENV")
    if virtual_env:
        return virtual_env

    # Fallback: check if sys.base_prefix differs from sys.prefix
    # (they differ when inside a venv)
    if hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix:
        return sys.prefix

    return None


def get_env_name(env_path: str) -> str:
    """
    Extract the environment name from its full path.

    Args:
        env_path: The full path to the virtual environment.

    Returns:
        The last component of the path (the folder name).
    """
    return os.path.basename(env_path)


def get_package_path() -> str | None:
    """
    Return the site-packages directory for the current environment.

    Returns:
        The first site-packages path available, or None if not found.
    """
    try:
        packages = site.getsitepackages()
        return packages[0] if packages else None
    except AttributeError:
        # site.getsitepackages() may not exist in all environments
        try:
            return site.getusersitepackages()
        except Exception:
            return None


def display_outside_matrix(python_path: str) -> None:
    """
    Print status and instructions when no virtual environment is detected.

    Args:
        python_path: The path to the current Python executable.
    """
    print("MATRIX STATUS: You're still plugged in")
    print(f"Current Python:      {python_path}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()
    print("To enter the construct, run:")
    print()
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\nScripts\nactivate       # On Windows")
    print()
    print("Then run this program again.")


def display_inside_construct(
    python_path: str,
    env_name: str,
    env_path: str,
    package_path: str | None,
) -> None:
    """
    Print status and details when inside a virtual environment.

    Args:
        python_path:  The path to the current Python executable.
        env_name:     The name of the active virtual environment.
        env_path:     The full path to the active virtual environment.
        package_path: The site-packages directory, or None if unavailable.
    """
    print("MATRIX STATUS: Welcome to the construct")
    print(f"Current Python:      {python_path}")
    print(f"Virtual Environment: {env_name}")
    print(f"Environment Path:    {env_path}")
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.")
    print()
    if package_path:
        print(f"Package installation path: {package_path}")
    else:
        print("Package installation path: (unavailable)")


def main() -> None:
    """
    Entry point: detect the environment and display the appropriate output.
    """
    python_path: str = sys.executable

    try:
        env_path: str | None = get_virtual_env_path()

        if env_path is None:
            # Running outside any virtual environment
            display_outside_matrix(python_path)
        else:
            # Running inside a virtual environment
            env_name: str = get_env_name(env_path)
            package_path: str | None = get_package_path()
            display_inside_construct(
                python_path, env_name, env_path, package_path
            )

    except Exception as e:
        # Graceful fallback for any unexpected errors
        print(f"ERROR: Unable to determine environment status: {e}",
              file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
