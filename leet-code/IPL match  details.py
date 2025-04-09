reverse_outcomes = {'win': 'loss', 'loss': 'win', 'draw': 'draw'}

def update_match_outcome(team_stats, team, outcome):
    outcomes = ['win', 'loss', 'draw']
    if not team_stats.get(team):
        team_stats[team] = {'win': 0, 'loss': 0, 'draw': 0}
    for possible_outcome in outcomes:
        if outcome == possible_outcome:
            team_stats[team][outcome] += 1
        else:
            team_stats[team][outcome] += 0

def get_points(team_stats, team):
    return team_stats[team]['win'] * 3 + team_stats[team]['draw']

def store_game_result(team_stats):
    t1, t2, match_outcome = input().split(';')
    update_match_outcome(team_stats, t1, match_outcome)
    update_match_outcome(team_stats, t2, reverse_outcomes[match_outcome])

def print_points_table(team_points, team_stats):
    team_fmt = 'Team: {}, Matches Played: {}, Won: {}, Lost: {}, Draw: {}, Points: {}'
    for points, team in team_points:
        won, lost, draw = team_stats[team]['win'], team_stats[team]['loss'], team_stats[team]['draw']
        matches_played = won + lost + draw
        output = team_fmt.format(team, matches_played, won, lost, draw, points)
        print(output)

def main():
    n = int(input())
    if n == 0:
        print("No Output")
        return
    team_stats = dict()
    for i in range(n):
        store_game_result(team_stats)
    team_points = []
    for team in team_stats:
        team_points.append((get_points(team_stats, team), team))
    team_points.sort(reverse=True)
    print_points_table(team_points, team_stats)

main()