import csv
from pprint import pprint


def read_nhl_teams(file_path):
    """Read the NHL teams data from a CSV file."""
    all_teams = []
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)

            for team in reader:
                # only get the 5on5 data,
                # otherwise you get duplicates.
                if team['situation'] == '5on5':
                    all_teams.append(team)
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    return all_teams

def sort_teams_by_stat(teams, column, reverse=True, top_n=10):
    """Sort the teams by a specific statistic and return the top N teams."""

    # a special function to get the value of the column we want to sort by
    def get_score(entry):
        return entry[column]

    sorted_teams = sorted(teams, key=get_score, reverse=reverse)

    data = []
    for team in sorted_teams:
        data.append({
            'Team': team['team'],
            column: team[column],
        })

    return sorted_teams[:top_n]


def main():
    file_path = 'data/nhl_teams_data_2024_2025.csv'
    teams = read_nhl_teams(file_path)

    # Get the column names from the first team
    columns = list(teams[0].keys())
    print("Available statistics to sort by:")
    for index, column in enumerate(columns):
        print(f"{index + 1}. {column}")

    choice = int(input("Enter the number of the statistic you want to sort by: ")) - 1
    COLUMN = columns[choice]

    # Sort the teams by the chosen statistic and print the top 5 teams
    top_teams = sort_teams_by_stat(teams, COLUMN)
    print(f"\nTop 5 NHL Teams by {COLUMN}:\n")
    for index, team in enumerate(top_teams):
        rank = index + 1
        print(f"{rank}. {team['team']} - {team[COLUMN]}")
if __name__ == "__main__":
    main()