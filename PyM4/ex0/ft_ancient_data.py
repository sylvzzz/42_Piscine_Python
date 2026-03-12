def ft_ancient_text() -> None:
    filename = "ancient_fragment.txt"
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print(f"Accessing Storage Vault: {filename}")
    try:
        f = open(filename)
        content = f.read()
        f.close()
        print("Connection established...")
        print("\nRECOVERED DATA:")
        print(content)
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


ft_ancient_text()
