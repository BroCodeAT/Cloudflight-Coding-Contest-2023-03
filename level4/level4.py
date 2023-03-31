import math

def load_file(filename: str = "level4/level4_1.in") -> list:
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
    left = ""
    while fighters:
        pairs.append(fighters[:2])
        fighters = fighters[2:]

    for pair in pairs:
        round_winner = check_winner(pair)
        left = left + round_winner
    return left


def check_tournament_winners(fighters: str) -> str:
    while len(fighters) > 1:
        fighters = tournament_round(fighters)
    return fighters


def write_to_file(data: list, filename: str = "level3/level3_1.out") -> None:
    with open(filename, "w") as file:
        for line in data:
            file.write(line + "\n")


def tournament(data: list) -> list:
    rounds = []
    for tourn in data[1:]:
        tourn = tourn.split(" ")
        rocks = "R" * int(tourn[0][:-1])
        papers = "P" * int(tourn[1][:-1])
        scissors = "S" * int(tourn[2][:-1])
        if rnd := gen_round(rocks, papers, scissors):
            rounds.append(rnd)
    return rounds

def fill_rocks(rocks, papers, players):
    start_pairs = ""
    div = 4
    while rocks:
        block = int(players/div)
        print(players)
        print(div)
        rest_rocks = len(rocks)
        if rest_rocks >= block-1:
            start_pairs += "P" + "R"*(block - 1)
            rocks = rocks[block - 1:]
            papers = papers[1:]
    
        if rest_rocks >= block:
            start_pairs += "R"*block
            rocks = rocks[block:]

        div *= 2
    return start_pairs, papers

def gen_round(rocks: str, papers: str, scissors: str) -> str:
    """Generate a round of the tournament"""
    players = len(rocks) + len(papers) + len(scissors)
    
    start_pairs, papers = fill_rocks(rocks, papers, players)


    while papers and scissors:
        start_pairs += "PS"
        papers = papers[1:]
        scissors = scissors[1:]

        if len(papers) >= 2:
            start_pairs += "PP"
            papers = papers[2:]

    while papers:
        start_pairs += "P"
        papers = papers[1:]

    while scissors:
        start_pairs += "S"
        scissors = scissors[1:]

    return start_pairs


if __name__ == '__main__':
    comp = tournament(load_file("level4/level4_example.in"))
    print(comp)
    write_to_file(comp, "level4/level4_example_our.out")
    for i in comp:
        print(check_tournament_winners(i))
    
    
    for i in range(1, 5 + 1):
        comp = tournament(load_file(f"level4/level4_{i}.in"))
        write_to_file(comp, f"level4/level4_{i}.out")
        for _ in comp:
            print(check_tournament_winners(_))
        
