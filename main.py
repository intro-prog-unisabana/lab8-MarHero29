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
    if sys.argv[1] == "--help":
    print("""Usage: python main.py <file_path> <command> [arguments]...

Commands:
    add "task"    - Add a task to the list.
    remove "task" - Remove a task from the list.
    view          - Display all tasks.

Examples:
    python main.py tasks.txt add "Buy groceries"
    python main.py tasks.txt remove "Do laundry"
    python main.py tasks.txt view
    python main.py tasks.txt add "Call mom" remove "Take out trash" view""")