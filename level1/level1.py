
def load_file(filename: str = "level1.in") -> list:
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]
    
def check_winner(styles: str) -> str:
    if "R" in styles and "P" in styles:
        return "P"
    elif "R" in styles and "S" in styles:
        return "R"
    elif "P" in styles and "S" in styles:
        return "S"
    elif styles[0] == styles[1]:
        return styles[0]
    
def write_to_file(winners: list) -> None:
    with open("level1.out", "w") as file:
        file.writelines(winners)