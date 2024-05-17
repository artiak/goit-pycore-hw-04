from typing import List


def read_lines(path: str) -> List[str]:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            content: str = file.read()
            
            return [line for line in content.splitlines() if line.strip()]

    except FileNotFoundError:
        print(f"Could not find file '{path}'")

        return []
    

# testing


def _test():
    pass_msg: str = "PASSED\n"

    print("Should handle file not found:")
    assert read_lines('xxx.txt') == []
    print(pass_msg)

    print("Should not consider emtpy line:")
    assert read_lines('empty.txt') == []
    print(pass_msg)


if __name__ == "__main__":
    _test()