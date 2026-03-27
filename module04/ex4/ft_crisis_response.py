def crisis_handler(filename: str) -> None:
    try:
        with open(filename) as file:
            content = file.read()
            print(f"SUCCESS: Archive recovered - ``{content}")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    except Exception as e:
        print(f"RESPONSE: {e}")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print("")
    filename1 = "lost_archive.txt"
    filename2 = "classified_vault.txt"
    filename3 = "standard_archive.txt"
    print(f"CRISIS ALERT: Attempting access to '{filename1}'...")
    crisis_handler(filename1)
    print("STATUS: Crisis handled, system stable")
    print("")
    print(f"CRISIS ALERT: Attempting access to '{filename2}'...")
    crisis_handler(filename2)
    print("STATUS: Crisis handled, security maintained")
    print("")
    print(f"ROUTINE ACCESS: Attempting access to '{filename3}'...")
    crisis_handler(filename3)
    print("STATUS: Normal operations resumed")
    print("")
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
