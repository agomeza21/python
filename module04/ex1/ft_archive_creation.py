def main() -> None:
    filename = "new_discovery.txt"
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print("")
    try:
        file = open(filename, "w")
        print(f"Initializing new storage unit: {filename}")
        print("Storage unit created successfully...")
    except PermissionError as p:
        print(f"Data inscription impossible: {p}")
        return
    print("")
    print("Inscribing preservation data...")
    file.write("[ENTRY 001] New quantum algorithm discovered\n")
    file.write("[ENTRY 002] Efficiency increased by 347%\n")
    file.write("[ENTRY 003] Archived by Data Archivist trainee\n")
    file.close()
    file = open(filename)
    print(file.read())
    print("")
    print("Data inscription complete. Storage unit sealed.")
    print(f"Archive '{filename}' ready for long-term preservation.")
    file.close()


if __name__ == "__main__":
    main()
