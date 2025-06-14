import sys
from typing import TextIO


def main() -> None:
    print("Todo list".center(20, "="))
    file: TextIO = load_file()
    display_tasks(file)
    while True:
        add_task(file)


def load_file() -> TextIO:
    """
    If tasks.txt exists => load file
    If it doesn't exist => create file and load
    """
    try:
        file = open("tasks.txt", "a+", encoding="utf-8")
        print("File opened".center(20, "-"))
    except Exception as e:
        print(f"Encountered unknown error: {e}")
        sys.exit(1)
    return file


def display_tasks(file: TextIO) -> None:
    print("Current tasks list: ")
    file.seek(0)  # Move pointer to beginning of stream
    lines: list[str] = file.readlines()
    if not lines:
        print("Tasks list is empty")
    else:
        for line in lines:
            print(line, end="")


def add_task(file: TextIO) -> None:
    new_task: str = input("Add new task: ")
    if new_task.lower() == "exit" or new_task.lower() == "quit":
        file.close()
        sys.exit()
    else:
        file.write(f"{new_task}\n")
        display_tasks(file)


if __name__ == "__main__":
    main()
