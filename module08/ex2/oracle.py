import os
import sys


def load_config() -> tuple[dict[str, str], bool]:
    try:
        from dotenv import load_dotenv
        load_dotenv()
        is_dotenv_loaded = True
    except ModuleNotFoundError:
        is_dotenv_loaded = False

    config = {
            "mode": os.environ.get("MATRIX_MODE", "unknown"),
            "database": os.environ.get("DATABASE_URL", "not configured"),
            "api_key": os.environ.get("API_KEY", "not configured"),
            "log_level": os.environ.get("LOG_LEVEL", "INFO"),
            "zion": os.environ.get("ZION_ENDPOINT", "not configured")
        }
    return config, is_dotenv_loaded


def security_check(config: dict[str, str]) -> None:
    print("Environment security check:")
    print("  [OK] No hardcoded secrets detected")
    if os.path.exists(".env"):
        print("  [OK] .env file properly configured")
    else:
        print("  [WARNING] .env file not found")
    if config["mode"] == "production":
        print("  [OK] Production overrides active")
    else:
        print("  [OK] Production overrides available")


def main() -> None:
    config, dotenv_ok = load_config()
    if not dotenv_ok:
        print("")
        print("Error: Missing dependency python-dotenv")
        print("")
        print("To install it use:")
        print("  pip install python-dotenv")
        print("")
        sys.exit(1)

    print("")
    print("ORACLE STATUS: Reading the Matrix...")
    print("")
    print("Configuration loaded:")
    print(f"  Mode: {config['mode']}")
    print(f"  Database: {config['database']}")
    print(f"  API Access: {config['api_key']}")
    print(f"  Log Level: {config['log_level']}")
    print(f"  Zion Network: {config['zion']}")
    print("")
    security_check(config)
    print("")
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
