def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    files = [
        "lost_archive.txt",
        "classified_vault.txt",
        "standard_archive.txt"
    ]

    for file in files:
        print(f"\nCRISIS ALERT: Attempting access to '{file}'...")

        try:
            with open(file, "r") as file:
                content = file.read()
                print(f"SUCCESS: Archive recovered - '{content}'")
                print("STATUS: Normal operations resumed")

        except FileNotFoundError:
            print("RESPONSE: Archive not found in storage matrix")
            print("STATUS: Crisis handled, system stable")

        except PermissionError:
            print("RESPONSE: Security protocols deny access")
            print("STATUS: Crisis handled, security maintained")
        except Exception as Error:
            print(f"RESPONSE: Unexpected system anomaly detected ({Error})")
            print("STATUS: Crisis handled, system stable")

    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
