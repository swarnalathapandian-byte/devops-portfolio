"""Tiny CI validation helper for demonstration purposes."""
from pathlib import Path


def validate_config(path: str) -> bool:
    """Return True when a config file exists and contains required keys."""
    file = Path(path)
    if not file.is_file():
        return False
    content = file.read_text(encoding="utf-8")
    return all(f"{key}=" in content for key in ("APP_NAME", "ENVIRONMENT"))


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()
    if not validate_config(args.path):
        parser.exit(1, "Config validation failed\n")
    print("Config validation passed")
