import json


def main():
    print('1 Добавить команду')
    print('2 Внести итоги матча')
    print('3 Сброс настроек')
    print('4 Выход')
    command = int(input(('Выберите действие, введя номер пункта (цифра от 1 до 4): ')))
    if command == 1:
        add_team()
    elif command == 2:
        add_match()
    elif command == 3:
        reset()
    elif command == 4:
        exit()
    else:
        print('Ошибка! Введите число от 1 до 4!')
    exit()


def add_team():
    with open('settings.json', 'r') as f:
        settings = json.load(f)
    f.close()
    teams = len(settings['teams'])
    name = str(input('Введите название команды: ')).title()
    settings['teams'][str(teams + 1)] = {'name': name, 'points': 0}
    with open('settings.json', 'w') as f:
        json.dump(settings, f, ensure_ascii=False, indent=4)
    f.close()


def add_match():
    with open('settings.json', 'r') as f:
        settings = json.load(f)
    f.close()
    teams = len(settings['teams'])
    matches = len(settings['matches'])
    name1 = str(input('Введите название команды 1: ')).title()
    name2 = str(input('Введите название команды 2: ')).title()
    team1_id, team2_id = None, None
    for i in settings['teams'].keys():
        if settings['teams'][i]['name'] == name1:
            team1_id = int(i)
        elif settings['teams'][i]['name'] == name2:
            team2_id = int(i)
    if team1_id and team2_id:
        print('Какая команда выйграла? (1 или 2)')
        print('Введите 0, если обе команды сыграли в ничью')
        result = int(input('Ввод: '))
        if result == 0 or result == 1 or result == 2:
            settings['matches'][str(matches + 1)] = {'team_ids': [team1_id, team2_id], 'result': result}
            with open('settings.json', 'w') as f:
                json.dump(settings, f, ensure_ascii=False, indent=4)
            f.close()
        else:
            print('Вводить можно только числа 0, 1, 2!')
            exit(1)
    else:
        print('Такой команды нет в настройках!')
        exit(1)


def reset():
    ask = str(input('Вы уверены? (Да/Нет): '))
    if ask.title() == "Да":
        with open('settings.json', 'w') as f:
            with open('default.json', 'r') as default:
                for i in default.readlines():
                    f.write(i)
            default.close()
        f.close()


main()