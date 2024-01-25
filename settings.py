import json

SETTINGS_FILE_PATH = 'settings.json'

OPTIONS = [
    '1 Добавить команду',
    '2 Внести итоги матча',
    '3 Сброс настроек',
    '4 Выход'
]

CONFIRMATION_MESSAGES = ['Да', 'Нет']

USER_INPUT_PROMPTS = [
    'Выберите действие, введя номер пункта (цифра от 1 до 4): ',
    'Какая команда выиграла? (1 или 2) \
    Введите 0, если обе команды сыграли в ничью: ',
    f'Вы уверены? ({CONFIRMATION_MESSAGES[0]}/{CONFIRMATION_MESSAGES[1]}): '
]

ERROR_MESSAGES = ['Ошибка! Введите число от 1 до 4!',
                  'Вводить можно только числа 0, 1, 2!']


def main():
    print_options()
    command = get_user_input()
    handle_command(command)


def print_options():
    for option in OPTIONS:
        print(option)


def get_user_input():
    try:
        return int(input(USER_INPUT_PROMPTS[0]))
    except ValueError:
        print(ERROR_MESSAGES[0])
        exit(1)


def handle_command(command):
    if command == 1:
        add_team()
    elif command == 2:
        add_match()
    elif command == 3:
        reset()
    elif command == 4:
        exit()
    else:
        print(ERROR_MESSAGES[0])
        exit(1)


def add_team():
    settings = load_settings()
    teams = len(settings['teams'])
    name = input('Введите название команды: ').title()
    settings['teams'][str(teams + 1)] = {'name': name, 'points': 0}
    save_settings(settings)


def add_match():
    settings = load_settings()
    matches = len(settings['matches'])
    name1 = input('Введите название команды 1: ').title()
    name2 = input('Введите название команды 2: ').title()
    team1_id, team2_id = find_team_ids(settings, name1, name2)

    if team1_id and team2_id:
        result = get_match_result()
        settings['matches'][str(matches + 1)] = {
            'team_ids': [team1_id, team2_id],
            'result': result
        }
        save_settings(settings)
    else:
        print('Такой команды нет в настройках!')
        exit(1)


def find_team_ids(settings, name1, name2):
    team1_id, team2_id = None, None
    for i, team_info in settings['teams'].items():
        if team_info['name'] == name1:
            team1_id = int(i)
        elif team_info['name'] == name2:
            team2_id = int(i)
    return team1_id, team2_id


def get_match_result():
    try:
        result = int(input(USER_INPUT_PROMPTS[1]))
        if result not in {0, 1, 2}:
            print(ERROR_MESSAGES[1])
            exit(1)
        return result
    except ValueError as e:
        print(e)
        exit(1)


def reset():
    ask = str(input(USER_INPUT_PROMPTS[2]))
    if ask.title() == CONFIRMATION_MESSAGES[0]:
        with open(SETTINGS_FILE_PATH, 'w') as f:
            with open('default.json', 'r') as default:
                f.writelines(default.readlines())


def load_settings(file_path=SETTINGS_FILE_PATH):
    with open(file_path, 'r') as file:
        settings = json.load(file)
    return settings


def save_settings(settings, file_path=SETTINGS_FILE_PATH):
    with open(file_path, 'w') as file:
        json.dump(settings, file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
