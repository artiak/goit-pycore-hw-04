from typing import Tuple, List
from util.file_reader import read_lines

def total_salary(path: str) -> Tuple[float, float]:
    lines: List[str] = read_lines(path)

    if not lines:
        return ()

    salaries: List[float] = _to_salaries(lines)

    total: float = sum(salaries)
    avarage: float = total / len(salaries)

    return total, avarage


def _to_salaries(lines: List[str]) -> List[float]:
    salaries: List[float] = []

    sal_idx = 1

    for line in lines:
        str_sal: str = line.split(',')[sal_idx]
        float_sal = _to_float(str_sal)

        if not float_sal:
            continue

        salaries.append(float_sal)

    return salaries


def _to_float(str_val: str) -> float:
    try:
        return float(str_val)

    except ValueError:
        print(f"Could not convert '{str_val}' to float")

        return None


# testing


pass_msg: str = "PASSED\n"

print("Should calculate total and average:")
tuple_sal: tuple = total_salary("task_01/salaries.txt")
assert tuple_sal[0] == 7000.5
assert tuple_sal[1] == 1750.125
print(pass_msg)
