def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("")

    filename = "classified_data.txt"
    try:
        with open(filename, "x") as file:
            file.write("[CLASSIFIED] Quantum encryption keys recovered\n")
            file.write("[CLASSIFIED] Archive integrity: 100%\n")
    except FileExistsError:
        pass

    try:
        with open(filename) as file:
            print("Initiating secure vault access...")
            print("Vault connection established with failsafe protocols")
            print("")
            print("SECURE EXTRACTION:")
            content = file.read()
            print(content)
            print("")
    except FileNotFoundError:
        print("Storage vault not found.")
        return

    try:
        with open(filename, "a") as file:
            new_entry = "[CLASSIFIED] New security protocols archived"
            print("SECURE PRESERVATION:")
            if new_entry not in content:
                file.write(new_entry)
                print(new_entry)
            else:
                print("Entry already exists in vault.")
    except PermissionError as p:
        print(f"Data inscription impossible: {p}")
        print("")
        print("Not all vault operations were completed.")
        return
    print("Vault automatically sealed upon completion")
    print("")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
