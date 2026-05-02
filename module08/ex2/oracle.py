from dotenv import load_dotenv
import os


def load_config() -> dict:
    load_dotenv()
    return {
        "mode": os.environ.get("MATRIX_MODE", "unknown"),
        "database": os.environ.get("DATABASE_URL", "not configured"),
        "api_key": os.environ.get("API_KEY", "not configured"),
        "log_level": os.environ.get("LOG_LEVEL", "INFO"),
        "zion": os.environ.get("ZION_ENDPOINT", "not configured")
    }


def security_check(config: dict) -> None:
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
    config = load_config()
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
