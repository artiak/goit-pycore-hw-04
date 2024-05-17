from colorama import Style
import sys
from pathlib import Path


def _obtain_path() -> str:
    if len(sys.argv) == 1:
        print("No command-line arguments foud")

        return None

    dir_path = sys.argv[1]
    print(f"Command-line argument: '{dir_path}'")

    return dir_path


def print_structure(folder_path, indent=0) -> None:
    if folder_path == None:
        return

    folder = Path(folder_path)

    _print_folder(indent, folder.name)

    for item in folder.iterdir():
        if not item.is_dir():
            _print_file(indent, item.name)

            continue

        print_structure(item, indent + 1)


def _print_folder(indent: int, name: str) -> None:
    print(Style.BRIGHT + "  " * indent + f"- {name}/")


def _print_file(indent: int, name: str) -> None:
    print(Style.DIM + "  " * (indent + 1) + f"- {name}")


# testing


print_structure(_obtain_path())
