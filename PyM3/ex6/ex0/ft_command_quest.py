import sys
if __name__ == "__main__":
    arguments = sys.argv
    program_name = sys.argv[0]
    args = sys.argv[1:]
    i = 1
    print("=== Command Quest ===")
    if len(sys.argv) == 1:
        print("No Arguments provided!")
        print(f"Program name: {program_name}")
    else:
        print(f"Program name: {program_name}")
        print(f"Arguments recived: {len(args)}")
        for arg in args:
            print(f"Argument {i}: {arg}")
            i += 1
    print(f"Total arguments: {i}")
