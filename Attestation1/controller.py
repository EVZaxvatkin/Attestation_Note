import datetime

import note
import repository
import utils

atr_of_note = {'id': '',
               'Дата': '',
               'Заголовок': '',
               'Содержание': ''}

list_of_notes = []


def view():
    global list_of_notes
    print('Выберете команду:\n'
          '   1 - Создать/добавить заметку,\n'
          '   2 - Просмотр заметок,\n'
          '   3 - Поиск заметки,\n'
          '   4 - Удаление заметки,\n'
          '   5 - Возврат в основное меню,\n'
          '   6 - Внести изменение в заметку,\n'
          '   7 - Выход')
    while True:
        choose = input('Введите номер команды: ')
        if choose == '1':
            title = input('Введите заголовок заметки: ')
            body = input('Введите текст заметки: ')
            object_note = note.Note(title, body)
            list_of_notes.append(dict(zip(atr_of_note, [object_note.get_id(),
                                                        str(object_note.get_create_date()).rsplit('.', 1)[0],
                                                        object_note.get_title(),
                                                        object_note.get_text()])))
            repository.save_notes(*list_of_notes)
            list_of_notes = []
            test = str(object_note.get_create_date()).rsplit('.', 1)[0]
            print(datetime.datetime.strptime(test, "%Y-%m-%d %H:%M:%S"))
        elif choose == '5':
            print('Выберете команду:\n'
            '   1 - Создать/добавить заметку,\n'
            '   2 - Просмотр заметок,\n'
            '   3 - Поиск заметки,\n'
            '   4 - Удаление заметки,\n'
            '   5 - Возврат в основное меню,\n'
            '   6 - Внести изменение в заметку,\n'
            '   7 - Выход')
        elif choose == '2':
            if not repository.read_notes():
                print('Заметка не найдена')
            else:
                for row in repository.read_notes():
                    list_of_notes.append(row)
                for your_note in sorted(list_of_notes, key=lambda item: int(item.get('id'))):
                    utils.print_dict(your_note)
            list_of_notes = []
        elif choose == '3':
            print('Команды поиска заметки:\n'
                  '   1 - Поиск по id,\n'
                  '   2 - Поиск по дате,\n'
                  '   3 - Выход')
            answer = input('Введите команду поиска: ')
            if answer == '1':
                index = input('Введите id: ')
                if not repository.get_by_id(index):
                    print(f'Заметка по id = {index} не найдена')
                else:
                    utils.print_dict(repository.get_by_id(index))
                print('Возврат в главное меню')
            elif answer == '2':
                regex = input('Введите дату: ')
                if not repository.get_by_date(regex):
                    print(f'Заметка за период = {regex} не найдена')
                else:
                    utils.print_dict(repository.get_by_date(regex))
                print('Возврат в главное меню')
            elif answer == '3':
                print('Возврат в главное меню')
            else:
                print('Данные введены не корректно')
                print('Возврат в главное меню')
        elif choose == '4':
            index = input('Введите номер id для удаления заметки: ')
            if not repository.delete_by_id(index):
                print(f'Заметка по id = {index} не найдена')
            else:
                print(f'Заметка успешно удалена')
            print('Возврат в главное меню')
        elif choose == '6':
            index = input('Введите id для изменения заметки: ')
            if not repository.get_by_id(index):
                print(f'Заметка по id = {index} не найдена')
            else:
                title = input('Введите заголовок заметки: ')
                body = input('Введите текст заметки: ')
                repository.delete_by_id(int(index))
                object_note = note.Note(title, body)
                repository.save_by_id(index,
                                      dict(zip(atr_of_note, [int(index),
                                                             str(object_note.get_create_date()).rsplit('.', 1)[0],
                                                             object_note.get_title(),
                                                             object_note.get_text()])))
        elif choose == '7':
            print('Всего доброго')
            break
        else:
            print('Данные введены не корректно')
