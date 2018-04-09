from nba_py import team, constants
from random import sample
from datetime import datetime


team_names = [constants.TEAMS[item]['name']for item in constants.TEAMS]
team_ids = [constants.TEAMS[item]['id']for item in constants.TEAMS]
team_dict = dict(zip(team_names, team_ids))
team_names = sample(team_names, len(team_names))


def get_roster(team_name, season):
    team_id = team_dict[team_name]
    team_roster = team.TeamCommonRoster(team_id, season).roster()
    return team_roster


def get_summary(team_name, season):
    team_id = team_dict[team_name]
    team_info = team.TeamSummary(team_id, season).info()
    return team_info


def seasons():
    seasons = []
    for x in range(1946, datetime.today().year + 1):
        x = str(x)
        y = int(x[-1]) + 1
        if y == 10:
            y = str(int(int(x[-2]) + 1) * 10)
            if y == '100':
                y = '00'
                seasons.append(x + '-' + y)
                continue
            seasons.append(x + '-' + y)
            continue
        else:
            seasons.append(x + '-' + x[2] + str(y))
    return seasons


if __name__ == "__main__":
    roster = get_roster('Kings', '2017-18')
    summary = get_summary('Kings', '2017-18')
