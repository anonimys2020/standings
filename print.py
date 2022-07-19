import json # импорт библиотеки


def load():
    with open('settings.json', 'r') as f: # открытие файла
        settings = json.load(f) # получение данных
    return settings


def main(settings):
    data = {}
    # Работа с json файлом. Получение.
    for i in settings['matches'].values():
        if i['result'] == 1:
            winner_id = i['team_ids'][0]
            settings['teams'][str(winner_id)]['points'] += 3
        elif i['result'] == 2:
            winner_id = i['team_ids'][1]
            settings['teams'][str(winner_id)]['points'] += 3
        elif i['result'] == 0:
            settings['teams'][str(i['team_ids'][0])]['points'] += 1
            settings['teams'][str(i['team_ids'][1])]['points'] += 1
        data[settings['teams'][str(i['team_ids'][0])]['name']] = settings['teams'][str(i['team_ids'][0])]['points']
        data[settings['teams'][str(i['team_ids'][1])]['name']] = settings['teams'][str(i['team_ids'][1])]['points']
    return data


def sort_dict(data):
    # Сортировка
    sorted_values = dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
    return sorted_values


def view(sorted_dict, settings):
    # Вывод
    keys = []
    for key in sorted_dict.keys():
        keys += [key]
    for i in range(len(keys)):
        print(f'{i + 1}. {keys[i]} - {sorted_dict[keys[i]]}')


view(sort_dict(main(load())), settings=load()) # запуск