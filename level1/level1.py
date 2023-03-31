def load_file(filename: str = "level1/level1_1.in") -> list:
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]


def write_to_file(data: list, filename: str = "level1/level1_1.out") -> None:
    with open(filename, "w") as file:
        for line in data:
            file.write(line + "\n")


def check_winner(styles: str) -> str:
    if "R" in styles and "P" in styles:
        return "P"
    elif "R" in styles and "S" in styles:
        return "R"
    elif "P" in styles and "S" in styles:
        return "S"
    elif styles[0] == styles[1]:
        return styles[0]


def competition(data: list) -> list:
    winner = []
    for fight in data[1:]:
        if win := check_winner(fight):
            winner.append(win)
    return winner


if __name__ == '__main__':
    for i in range(1, 6):
        comp = competition(load_file(f"level1/level1_{i}.in"))
        write_to_file(comp, f"level1/level1_{i}.out")
