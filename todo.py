import os
import sys
import time


def main() -> None:
    print(
        f"\
    {'=' * 10}\n\
    To-Do list\n\
    {'=' * 10}\n\n\
    Main Menu: \n\
    1. View To-Do List\n\
    2. Add New Task\n\
    3. Exit Program"
    )
    data = load_file()
    while True:
        menu_input = input("\nSelect a number to continue: ")
        if menu_input == "1":
            display_tasks(data)
        elif menu_input == "2":
            add_task(data)
        elif menu_input == "3":
            break
        else:
            print("Invalid option! Choose between 1, 2 and 3")

    print("Goodbye!")
    time.sleep(1)
    sys.exit()


def load_file(filename: str = "tasks.txt") -> list:
    """
    If tasks.txt doesn't exist => create new file / Else, move on
    Open file => store in local memory for use
    """
    todo_list = []
    if not os.path.exists(filename):
        try:
            open(filename, "w", encoding="utf-8").close()
        except PermissionError as e:
            print(f"Not permitted to create new file: {e}")
        except OSError as e:
            print(f"OS-level failure: {e}")
            sys.exit(1)

    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f.readlines():
                todo_list.append(
                    line.strip()
                )  # readlines() adds a newline at the end of each string by default
    except OSError as e:
        print(f"OS-level failure: {e}")
        sys.exit(1)

    return todo_list


def display_tasks(data: list[str]) -> None:
    print("Current to-do list:")
    if not data:
        print("To-do list is empty")
    else:
        for d in data:
            print(d)


def add_task(data: list[str], filename: str = "tasks.txt") -> None:
    new_task: str = input("Add new task: ")
    data.append(new_task)
    with open(filename, "w", encoding="utf-8") as f:
        for d in data:
            f.write(f"{d}\n")


if __name__ == "__main__":
    main()
