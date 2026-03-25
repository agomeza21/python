def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print("")
    try:
        file = open("ancient_fragment.txt")
        print("Accessing Storage Vault: ancient_fragment.txt")
        print("Connection established...")
    except FileNotFoundError:
        print("Storage vault not found.")
        print("")
        print("Not able to start data recovery.")
        return
    print("")
    print("RECOVERED DATA:")
    print(file.read())
    print("")
    print("Data recovery complete. Storage unit disconnected.")
    file.close()


if __name__ == "__main__":
    main()
