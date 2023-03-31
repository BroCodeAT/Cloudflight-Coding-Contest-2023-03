
def load_file(filename: str = "level1.in") -> list:
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]


def load_multiple_files(form: str = "level%.in", count: int = 1) -> list:
    return [load_file(form.replace("%", str(count))) for i in range(1, count + 1)]
