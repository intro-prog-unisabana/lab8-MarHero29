import sys
from todo_manager import read_todo_file, write_todo_file

try:
    if len(sys.argv) < 2:
        raise IndexError("Insufficient arguments provided!")

    if sys.argv[1] == "--help":
        print("""Usage: python main.py <file_path> <command> [arguments]...""")

    else:
        file_path = sys.argv[1]
        tasks = read_todo_file(file_path)

except (IndexError, ValueError) as e:
    print(e)