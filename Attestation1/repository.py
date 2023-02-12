import json

FILENAME = 'db.json'


def save_notes(*args):
    temp = []
    for item in args:
        temp.append(item)
    for item in read_notes():
        temp.append(item)
    with open(FILENAME, 'w', encoding='utf-8') as outfile:
        json.dump(temp, outfile, indent=4)


def read_notes():
    try:
        with open(FILENAME, 'r') as file:
            result = json.load(file)
        return result
    except FileNotFoundError:
        result = []
        return result


def get_by_id(note_id):
    try:
        for note in read_notes():
            if note.get('id') == int(note_id):
                return note
    except ValueError:
        return None


def get_by_date(regex):
    result = []
    for note in read_notes():
        if regex in note.get('Added'):
            result.append(note)
    return result


def save_by_id(note_id, dict_about_note):
    list_of_dicts = []
    for item in read_notes():
        if item.get('id') != int(note_id):
            list_of_dicts.append(item)
    list_of_dicts.append(dict_about_note)
    with open(FILENAME, 'w', encoding='utf-8') as outfile:
        json.dump(list_of_dicts, outfile, indent=4)


def find_max_id():
    max_id = 0
    for item in read_notes():
        if max_id < item.get('id'):
            max_id = item.get('id')
    return max_id


def delete_by_id(note_id):
    temp = []
    flag = False
    try:
        for unit in read_notes():
            if unit.get('id') == int(note_id):
                flag = True
            if unit.get('id') != int(note_id):
                temp.append(unit)
        with open(FILENAME, 'w', encoding='utf-8') as outfile:
            json.dump(temp, outfile, indent=4)
        return flag
    except ValueError:
        return flag
