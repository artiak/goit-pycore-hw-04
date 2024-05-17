from typing import List, Dict, Union
from util.file_reader import read_lines


ID_KEY: str = "id"
NAME_KEY: str = "name"
AGE_KEY: str = "age"


def get_cats_info(path: str) -> List[Dict[str, Union[str, int]]]:
    lines: List[str] = read_lines(path)

    if not lines:
        return ()

    id_idx: int = 0
    name_idx: int = 1
    age_idx: int = 2

    cats: List[Dict[str, Union[str, int]]] = []

    for line in lines:
        list_cat: List[str] = line.split(",")

        if not list_cat:
            continue

        dict_cat: Dict[str, Union[str, int]] = {}

        dict_cat[ID_KEY] = list_cat[id_idx]
        dict_cat[NAME_KEY] = list_cat[name_idx]
        dict_cat[AGE_KEY] = _to_int(list_cat[age_idx])

        cats.append(dict_cat)

    return cats


def _to_int(str_val: str) -> int:
    try:
        return int(str_val)

    except ValueError:
        print(f"Could not convert '{str_val}' to int")

        return None


# testing


PASS_MSG: str = "PASSED\n"

print("Should read cat props:")
cat: dict = get_cats_info('task_02/cats.txt')[0]
assert cat[ID_KEY] == "60b90c1c13067a15887e1ae1"
assert cat[NAME_KEY] == "Tayson"
assert cat[AGE_KEY] == 3
print(PASS_MSG)
