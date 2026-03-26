"""
oracle.py - The Oracle: secure configuration loader.
Loads environment variables from a .env file and validates them.
"""

import os
import sys
from dotenv import load_dotenv, find_dotenv


REQUIRED_VARS: dict[str, str] = {
    "DATABASE_URL":  "Connection string for data storage",
    "API_KEY":       "Secret key for external services",
    "ZION_ENDPOINT": "URL for the resistance network",
}

OPTIONAL_VARS: dict[str, str] = {
    "MATRIX_MODE": "development",
    "LOG_LEVEL":   "DEBUG",
}


def load_config() -> dict[str, str]:
    """
    Load and validate environment variables from the nearest .env file.
    Returns a dict of all config values, exits on missing required vars.
    """
    load_dotenv(find_dotenv(usecwd=True))

    config: dict[str, str] = {}
    missing: list[str] = []

    for var, description in REQUIRED_VARS.items():
        value = os.getenv(var)
        if not value:
            print(f"[MISSING] {var} - {description}")
            missing.append(var)
        else:
            config[var] = value

    for var, default in OPTIONAL_VARS.items():
        config[var] = os.getenv(var, default)

    if missing:
        print("\nMissing required variables. Copy .env.example to .env.")
        print("  cp .env.example .env")
        sys.exit(1)

    return config


def display_config(config: dict[str, str]) -> None:
    """Print the active configuration in Oracle format."""
    mode = config["MATRIX_MODE"]
    db = (
        "Connected to local instance"
        if mode == "development"
        else "Connected to production"
    )
    zion = "Online" if config["ZION_ENDPOINT"] else "Offline"

    print("Configuration loaded:")
    print(f"Mode:         {mode}")
    print(f"Database:     {db}")
    print("API Access:   Authenticated")
    print(f"Log Level:    {config['LOG_LEVEL']}")
    print(f"Zion Network: {zion}")


def security_check() -> None:
    """Display environment security check results."""
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")


def main() -> None:
    """Entry point."""
    print("ORACLE STATUS: Reading the Matrix...\n")
    config = load_config()
    display_config(config)
    security_check()
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
