import sys


def ft_stream_management() -> None:
    sys.stdout.write("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n\n")
    sys.stdout.write("Input Stream active. Enter archivist ID: ")
    archivist_id = input()
    sys.stdout.write("Input Stream active. Enter status report: ")
    status_report = input()
    print()
    sys.stdout.write(f'[STANDARD] Archive status from '
                     f'{archivist_id}: {status_report}\n')
    sys.stderr.write("[ALERT] System diagnostic: "
                     "Communication channels verified\n")
    sys.stdout.write("[STANDARD] Data transmission complete\n")
    sys.stdout.write("\nThree-channel communication test successful\n")


ft_stream_management()
