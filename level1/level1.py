
def load_file(filename: str = "level1.in") -> list:
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]
    
