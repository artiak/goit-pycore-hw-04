import sys
from typing import Tuple, Any, Dict, List


name_to_phone: Dict[str, str] = {}

cmd_to_func: Dict[str, str] = {}
cmd_to_func["hello"] = "_greet"
cmd_to_func["add"] = "_add_contact"
cmd_to_func["change"] = "_change_contact"
cmd_to_func["phone"] = "_show_phone"
cmd_to_func["all"] = "_show_all"
cmd_to_func["close"] = "_exit"
cmd_to_func["exit"] = "_exit"


def main():
    while True:
        str_input: str = input("Please enter a command with arguments: ")
        tuple_input: Tuple[str, list] = _parse_input(str_input)

        cmd: str = tuple_input[0]

        if not cmd in cmd_to_func:
            print("Invalid command\n")
            continue

        args: list = tuple_input[1]

        _call_function(cmd, args)


def _parse_input(input: str) -> Tuple[str, list]:
    list_input: List[str] = input.strip().split()

    func = list_input[0].lower()
    args = list_input[1:]

    return (func, args)


def _call_function(cmd: str, args: tuple) -> None:
    func: str = cmd_to_func[cmd]
    globs: Dict[str, Any] = globals()

    if not _is_function(func, globs):
        print(f"Function '{func}' not found\n")

        return

    try:
        globs[func](*args)
    except TypeError as err:
        print(err)
        print("")


def _is_function(name: str, globs: Dict[str, Any]) -> bool:
    return name in globs and callable(globs[name])


def _greet() -> None:
    print("How can I help you?\n")


def _add_contact(name: str, phone: str) -> None:
    name_to_phone[name] = phone
    print("Contact added\n")


def _change_contact(name: str, phone: str) -> None:
    if not name in name_to_phone:
        print("Contact not foud\n")

        return

    name_to_phone[name] = phone
    print("Contact updated\n")


def _show_phone(name: str) -> None:
    if not name in name_to_phone:
        print("Contact not foud\n")

        return

    print(name_to_phone[name])


def _show_all() -> None:
    for name, phone in name_to_phone.items():
        print(name + " : " + phone)

    print("\n")


def _exit() -> None:
    print("Good bye\n")

    sys.exit(0)


# testing


main()
