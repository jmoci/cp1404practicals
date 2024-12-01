from itertools import count

FILE_PATH = "wimbledon.csv"
CHAMPION_INDEX = 2
CHAMPION_COUNTRY_INDEX = 3
def main():
    competitions = []
    read_competitions(competitions)
    champion_to_wins = get_champions_to_wins(competitions)
    countries = get_winning_countries(competitions)
    display_stats(champion_to_wins, countries)

def display_stats(champions_to_wins, countries):
    print("Wimbledon Champions:")
    for champion,wins in champions_to_wins.items():
        print(f"{champion} {wins}")
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


def get_winning_countries(competitions):
    countries = set()
    for competition in competitions:
        countries.add(competition[CHAMPION_COUNTRY_INDEX])
    return countries

def get_champions_to_wins(competitions):
    champion_to_wins = {}
    for competition in competitions:
        champion = competition[CHAMPION_INDEX]
        if champion not in champion_to_wins:
            champion_to_wins[champion] = 1
        else:
            champion_to_wins[champion] += 1
    return champion_to_wins

def read_competitions(competitions):
    with open(FILE_PATH, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            competitions.append(line.strip().split(","))
main()