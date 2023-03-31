
def load_file(filename: str = "level4.in") -> list:
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]