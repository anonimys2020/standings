import json

SETTINGS_FILE_PATH = 'settings.json'


def load_settings(file_path=SETTINGS_FILE_PATH):
    """
    Load settings from a JSON file.

    Args:
        file_path (str): The path to the JSON file. Default is 'settings.json'.

    Returns:
        dict: Loaded settings.
    """
    with open(file_path, 'r') as file:
        settings = json.load(file)
    return settings


def calculate_points(settings):
    """
    Calculate points for teams based on match results in the settings.

    Args:
        settings (dict): Loaded settings.

    Returns:
        dict: Dictionary with team names as keys and their points as values.
    """
    team_points = {}
    for match_info in settings['matches'].values():
        for result, team_id in zip(match_info['result'],
                                   match_info['team_ids']):
            team_id_str = str(team_id)
            points = 3 if result in {1, 2} else 1
            settings['teams'][team_id_str]['points'] += points

            team_points[settings['teams'][team_id_str]['name']] = \
                settings['teams'][team_id_str]['points']

    return team_points


def sort_team_points(team_points):
    """
    Sort team points in descending order.

    Args:
        team_points (dict): Team names as keys and their points as values.

    Returns:
        dict: Sorted team points in descending order.
    """
    return dict(
        sorted(team_points.items(), key=lambda x: x[1], reverse=True)
    )


def display_sorted_team_points(sorted_team_points):
    """
    Display the sorted team points with rankings.

    Args:
        sorted_team_points (dict): Sorted team points in descending order.
    """
    for rank, (team_name, points) in enumerate(sorted_team_points.items(),
                                               start=1):
        print(f'{rank}. {team_name} - {points}')


if __name__ == '__main__':
    # Load settings, calculate and sort team points, then display
    settings_data = load_settings()
    team_points_data = calculate_points(settings_data)
    display_sorted_team_points(sort_team_points(team_points_data))
