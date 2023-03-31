
def load_file(filename: str = "level1/level1_1.in") -> list:
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

def tournament_round(fighters: str) -> str:
    pairs = []
    while fighters:
        pairs.append(fighters[:2])
        fighters = fighters[2:]

    for pair in pairs:
        round_winner = check_winner(pair)
        left = left + round_winner
    return left

def check_tournament_winners(fighters: str, m: int) -> str:
    fighters_for_second = tournament_round(fighters)
    return tournament_round(fighters_for_second)





def write_to_file(data: list, filename: str = "level1/level1_1.out") -> None:
    with open(filename, "w") as file:
        for line in data:
            file.write(line + "\n")


def tournament(data: list) -> list:
    winner = []
    for tourn in data[1:]:
        if win := check_tournament_winners(tourn):
            winner.append(win)
    return winner


if __name__ == '__main__':
    for i in range(1, 5):
        comp = tournament(load_file(f"level2/level2_{i}.in"))
        write_to_file(comp, f"level2/level2_{i}.out")
