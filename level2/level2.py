
def load_file(filename: str = "level2.in") -> list:
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

def check_tournament_winners(fighters: str, m: int) -> str:
    fighters_for_second = tournament_round(fighters)
    return tournament_round(fighters_for_second)


